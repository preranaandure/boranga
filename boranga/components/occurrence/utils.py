import json
import logging
import os
from zipfile import ZipFile

import geopandas as gpd
from django.apps import apps
from django.conf import settings
from django.contrib.gis.gdal import SpatialReference
from django.contrib.gis.geos import GEOSGeometry
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from boranga.components.main.utils import feature_json_to_geosgeometry
from boranga.components.occurrence.email import (
    send_external_submit_email_notification,
    send_submit_email_notification,
)
from boranga.components.occurrence.models import (
    OccurrenceReport,
    OccurrenceReportAmendmentRequest,
    OccurrenceReportGeometry,
    OccurrenceReportUserAction,
)
from boranga.components.occurrence.serializers import (
    OccurrenceReportGeometrySaveSerializer,
)
from boranga.ledger_api_utils import retrieve_email_user

logger = logging.getLogger(__name__)


def save_geometry(request, instance, geometry_data):
    if not geometry_data:
        logger.warn("No Occurrence Report geometry to save")
        return

    geometry = json.loads(geometry_data)
    if (
        0 == len(geometry["features"])
        and 0
        == OccurrenceReportGeometry.objects.filter(occurrence_report=instance).count()
    ):
        # No feature to save and no feature to delete
        logger.warn("OccurrenceReport geometry has no features to save or delete")
        return

    action = request.data.get("action", None)

    geometry_ids = []
    for feature in geometry.get("features"):
        supported_geometry_types = ["MultiPolygon", "Polygon", "MultiPoint", "Point"]
        geometry_type = feature.get("geometry").get("type")
        # Check if feature is of a supported type, continue if not
        if geometry_type not in supported_geometry_types:
            logger.warn(
                f"OccurrenceReport: {instance} contains a feature that is not a "
                f"{' or '.join(supported_geometry_types)}: {feature}"
            )
            continue

        logger.info(
            f"Processing OccurrenceReport {instance} geometry feature type: {geometry_type}"
        )

        geom_4326 = feature_json_to_geosgeometry(feature)

        original_geometry = feature.get("properties", {}).get("original_geometry")
        srid_original = original_geometry.get("properties", {}).get("srid", 4326)
        if not srid_original:
            raise ValidationError(
                f"Geometry must have an SRID set: {original_geometry.get('coordinates', [])}"
            )

        if not original_geometry.get("type", None):
            original_geometry["type"] = geometry_type
        feature_json = {"type": "Feature", "geometry": original_geometry}
        geom_original = feature_json_to_geosgeometry(feature_json, srid_original)

        geoms = [(geom_4326, geom_original)]

        for geom in geoms:
            geometry_data = {
                "occurrence_report_id": instance.id,
                "geometry": geom[0],
                "original_geometry_ewkb": geom[1].ewkb,
                # TODO: Add intersects condition
                # "intersects": True,  # probably redunant now that we are not allowing non-intersecting geometries
            }
            if feature.get("id"):
                logger.info(
                    f"Updating existing OccurrenceReport geometry: {feature.get('id')} for Report: {instance}"
                )
                try:
                    geometry = OccurrenceReportGeometry.objects.get(
                        id=feature.get("id")
                    )
                except OccurrenceReportGeometry.DoesNotExist:
                    logger.warn(
                        f"OccurrenceReport geometry does not exist: {feature.get('id')}"
                    )
                    continue
                geometry_data["drawn_by"] = geometry.drawn_by
                geometry_data["locked"] = (
                    action in ["submit"]
                    and geometry.drawn_by == request.user.id
                    or geometry.locked
                )
                serializer = OccurrenceReportGeometrySaveSerializer(
                    geometry, data=geometry_data
                )
            else:
                logger.info(f"Creating new geometry for OccurrenceReport: {instance}")
                geometry_data["drawn_by"] = request.user.id
                geometry_data["locked"] = action in ["submit"]
                serializer = OccurrenceReportGeometrySaveSerializer(data=geometry_data)

            serializer.is_valid(raise_exception=True)
            ocr_geometry_instance = serializer.save()
            logger.info(f"Saved OccurrenceReport geometry: {ocr_geometry_instance}")
            geometry_ids.append(ocr_geometry_instance.id)

    # Remove any ocr geometries from the db that are no longer in the ocr_geometry that was submitted
    # Prevent deletion of polygons that are locked after status change (e.g. after submit)
    # or have been drawn by another user
    deleted_geometries = (
        OccurrenceReportGeometry.objects.filter(occurrence_report=instance)
        .exclude(Q(id__in=geometry_ids) | Q(locked=True) | ~Q(drawn_by=request.user.id))
        .delete()
    )
    if deleted_geometries[0] > 0:
        logger.info(
            f"Deleted OccurrenceReport geometries: {deleted_geometries} for {instance}"
        )


@transaction.atomic
def ocr_proposal_submit(ocr_proposal, request):
    if not ocr_proposal.can_user_edit:
        raise ValidationError(
            "You can't submit this report at the moment due to the status or a permission issue"
        )

    ocr_proposal.submitter = request.user.id
    ocr_proposal.lodgement_date = timezone.now()

    # Set the status of any pending amendment requests to 'amended'
    ocr_proposal.amendment_requests.filter(
        status=OccurrenceReportAmendmentRequest.STATUS_CHOICE_REQUESTED
    ).update(status=OccurrenceReportAmendmentRequest.STATUS_CHOICE_AMENDED)

    # Create a log entry for the proposal
    ocr_proposal.log_user_action(
        OccurrenceReportUserAction.ACTION_LODGE_PROPOSAL.format(ocr_proposal.id),
        request,
    )

    # Create a log entry for the user
    submitter = retrieve_email_user(ocr_proposal.submitter)
    if submitter:
        submitter.log_user_action(
            OccurrenceReportUserAction.ACTION_LODGE_PROPOSAL.format(ocr_proposal.id),
            request,
        )

    ret1 = send_submit_email_notification(request, ocr_proposal)
    ret2 = send_external_submit_email_notification(request, ocr_proposal)

    if (settings.WORKING_FROM_HOME and settings.DEBUG) or ret1 and ret2:
        ocr_proposal.processing_status = (
            OccurrenceReport.PROCESSING_STATUS_WITH_ASSESSOR
        )
        ocr_proposal.customer_status = OccurrenceReport.PROCESSING_STATUS_WITH_ASSESSOR
        ocr_proposal.documents.all().update(can_delete=False)
        ocr_proposal.save()
    else:
        raise ValidationError(
            "An error occurred while submitting occurrence report (Submit email notifications failed)"
        )

    return ocr_proposal


def save_document(request, instance, comms_instance, document_type, input_name=None):
    if "filename" in request.data and input_name:
        filename = request.data.get("filename")
        _file = request.data.get("_file")

        if document_type == "shapefile_document":
            document = instance.shapefile_documents.get_or_create(
                input_name=input_name, name=filename
            )[0]
        else:
            raise ValidationError(f"Invalid document type {document_type}")

        document._file = _file
        document.save()


@transaction.atomic
def delete_document(request, instance, comms_instance, document_type, input_name=None):
    document_id = request.data.get("document_id", None)
    if document_id:
        if document_type == "shapefile_document":
            document = instance.shapefile_documents.get(id=document_id)
        else:
            raise ValidationError(f"Invalid document type {document_type}")

        if not document:
            raise ValidationError(f"Document id {document_id} not found")

        if document._file and os.path.isfile(document._file.path):
            os.remove(document._file.path)

        document.delete()


@transaction.atomic
def process_shapefile_document(request, instance, *args, **kwargs):
    action = request.data.get("action")
    input_name = request.data.get("input_name")
    document_type = "shapefile_document"
    request.data.get("document_id")
    comms_instance = None

    if action == "list":
        pass
    elif action == "delete":
        delete_document(request, instance, comms_instance, document_type, input_name)
    elif action == "save":
        save_document(request, instance, comms_instance, document_type, input_name)
    else:
        raise ValidationError(f"Invalid action {action} for shapefile document")

    documents_qs = instance.shapefile_documents

    returned_file_data = [
        dict(
            url=d.path,
            id=d.id,
            name=d.name,
        )
        for d in documents_qs.filter(input_name=input_name)
        if d._file
    ]
    return {"filedata": returned_file_data}


def extract_attached_archives(instance, foreign_key_field=None):
    """Extracts shapefiles from attached zip archives and saves them as shapefile documents."""

    archive_files_qs = instance.shapefile_documents.filter(Q(name__endswith=".zip"))
    instance_name = instance._meta.model.__name__
    shapefile_archives = [qs._file for qs in archive_files_qs]
    # TODO: Upload multiple archives
    for archive in shapefile_archives:
        archive_path = os.path.dirname(archive.path)
        z = ZipFile(archive.path, "r")
        z.extractall(archive_path)

        for zipped_file in z.filelist:
            shapefile_model = apps.get_model(
                "boranga", f"{instance_name}ShapefileDocument"
            )
            shapefile_model.objects.create(
                **{
                    foreign_key_field: instance,
                    "name": zipped_file.filename,
                    "input_name": "shapefile_document",
                    "_file": f"{archive_path}/{zipped_file.filename}",
                }
            )

    return archive_files_qs


def validate_map_files(request, instance, foreign_key_field=None):
    # Validates shapefiles uploaded with via the proposal map or the competitive process map.
    # Shapefiles are valid when the shp, shx, and dbf extensions are provided
    # and when they intersect with DBCA legislated land or water polygons

    valid_geometry_saved = False

    logger.debug(f"Shapefile documents: {instance.shapefile_documents.all()}")

    if not instance.shapefile_documents.exists():
        raise ValidationError(
            "Please attach at least a .shp, .shx, and .dbf file (the .prj file is optional but recommended)"
        )

    archive_files_qs = extract_attached_archives(instance, foreign_key_field)

    # Shapefile extensions shp (geometry), shx (index between shp and dbf), dbf (data) are essential
    shp_file_qs = instance.shapefile_documents.filter(
        Q(name__endswith=".shp")
        | Q(name__endswith=".shx")
        | Q(name__endswith=".dbf")
        | Q(name__endswith=".prj")
    )

    # Validate shapefile and all the other related files are present
    if not shp_file_qs and not archive_files_qs:
        raise ValidationError(
            "You can only attach files with the following extensions: .shp, .shx, and .dbf or .zip"
        )

    shp_files = shp_file_qs.filter(name__endswith=".shp").distinct()
    shp_file_basenames = [s[:-4] for s in shp_files.values_list("name", flat=True)]

    shx_files = shp_file_qs.filter(name__in=[f"{b}.shx" for b in shp_file_basenames])
    dbf_files = shp_file_qs.filter(name__in=[f"{b}.dbf" for b in shp_file_basenames])

    # Check if no required files are missing
    if any(f == 0 for f in [shp_files.count(), shx_files.count(), dbf_files.count()]):
        raise ValidationError(
            "Please attach at least a .shp, .shx, and .dbf file (the .prj file is optional but recommended)"
        )
    # Check if all files have the same count
    if not (shp_files.count() == shx_files.count() == dbf_files.count()):
        raise ValidationError(
            "Please attach at least a .shp, .shx, and .dbf file "
            "(the .prj file is optional but recommended) for every shapefile"
        )

    # Add the shapefiles to a zip file for archiving purposes
    # (as they are deleted after being converted to proposal geometry)
    shapefile_archive_name = (
        os.path.splitext(instance.shapefile_documents.first().path)[0]
        + "-"
        + timezone.now().strftime("%Y%m%d%H%M%S")
        + ".zip"
    )
    shapefile_archive = ZipFile(shapefile_archive_name, "w")
    for shp_file_obj in shp_file_qs:
        shapefile_archive.write(shp_file_obj.path, shp_file_obj.name)
    shapefile_archive.close()

    # A list of all uploaded shapefiles
    shp_file_objs = shp_file_qs.filter(Q(name__endswith=".shp"))

    for shp_file_obj in shp_file_objs:
        gdf = gpd.read_file(shp_file_obj.path)  # Shapefile to GeoDataFrame

        if gdf.empty:
            raise ValidationError(f"Geometry is empty in {shp_file_obj.name}")

        # If no prj file assume WGS-84 datum
        if not gdf.crs:
            gdf_transform = gdf.set_crs("epsg:4326", inplace=True)
        else:
            gdf_transform = gdf.to_crs("epsg:4326")

        geometries = gdf_transform.geometry  # GeoSeries

        # Only accept points or polygons
        geom_type = geometries.geom_type.values[0]
        if geom_type not in ("Point", "MultiPoint", "Polygon", "MultiPolygon"):
            raise ValidationError(f"Geometry of type {geom_type} not allowed")

        # Check for intersection with DBCA geometries
        gdf_transform["valid"] = False
        for geom in geometries:
            srid = SpatialReference(
                geometries.crs.srs
            ).srid  # spatial reference identifier

            geometry = GEOSGeometry(geom.wkt, srid=srid)

            # Add the file name as identifier to the geojson for use in the frontend
            if "source_" not in gdf_transform:
                gdf_transform["source_"] = shp_file_obj.name

            gdf_transform["valid"] = True

            # Some generic code to save the geometry to the database
            # That will work for both a proposal instance and a competitive process instance
            instance_name = instance._meta.model.__name__
            if not foreign_key_field:
                foreign_key_field = instance_name.lower()

            geometry_model = apps.get_model("boranga", f"{instance_name}Geometry")
            geometry_model.objects.create(
                **{
                    foreign_key_field: instance,
                    "polygon": (
                        geometry if geom_type in ["Polygon", "MultiPolygon"] else None
                    ),
                    "point": geometry if geom_type in ["Point", "MultiPoint"] else None,
                    "intersects": True,
                    "drawn_by": request.user.id,
                }
            )

        instance.save()
        valid_geometry_saved = True

    # Delete all shapefile documents so the user can upload another one if they wish.
    instance.shapefile_documents.all().delete()

    return valid_geometry_saved
