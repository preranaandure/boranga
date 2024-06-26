from django.contrib.gis import admin, forms
from django.contrib.gis.geos import GEOSGeometry

import nested_admin

from boranga.components.occurrence.models import (
    AnimalHealth,
    BufferGeometry,
    CoordinationSource,
    CountedSubject,
    Datum,
    DeathReason,
    Drainage,
    IdentificationCertainty,
    Intensity,
    LandForm,
    LocationAccuracy,
    ObservationMethod,
    Occurrence,
    OccurrenceGeometry,
    OccurrenceReportGeometry,
    OccurrenceReport,
    OccurrenceTenure,
    OccurrenceTenurePurpose,
    PermitType,
    PlantCondition,
    PlantCountAccuracy,
    PlantCountMethod,
    PrimaryDetectionMethod,
    ReproductiveState,
    RockType,
    SampleDestination,
    SampleType,
    SecondarySign,
    SoilColour,
    SoilCondition,
    SoilType,
    WildStatus,
)
from boranga.components.spatial.utils import (
    transform_geosgeometry_3857_to_4326,
    wkb_to_geojson,
)


class GeometryField(forms.GeometryField):
    widget = forms.OSMWidget(
        attrs={
            "display_raw": False,
            "map_width": 800,
            "map_srid": 4326,
            "map_height": 600,
            "default_lat": -31.9502682,
            "default_lon": 115.8590241,
        }
    )


class OccurrenceTenureInline(nested_admin.NestedTabularInline):
    model = OccurrenceTenure
    extra = 0
    verbose_name = "Occurrence Geometry Tenure Area"
    verbose_name_plural = "Occurrence Geometry Tenure Areas"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "tenure_area_id",
                    "status",
                    "owner_name",
                    "owner_count",
                    "purpose",
                    "significant_to_occurrence",
                    "comments",
                )
            },
        ),
    )

    readonly_fields = ["tenure_area_id"]


class BufferGeometryInlineForm(forms.ModelForm):
    geometry = GeometryField()

    class Meta:
        model = BufferGeometry
        fields = "__all__"


class BufferGeometryInline(nested_admin.NestedStackedInline):
    model = BufferGeometry
    form = BufferGeometryInlineForm
    extra = 0

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "geometry",
                    ("original_geometry"),
                    (
                        "area_sqm",
                        "area_sqhm",
                    ),
                    (
                        "object_id",
                        "content_type",
                        "created_from",
                        "source_of",
                    ),
                )
            },
        ),
    )

    readonly_fields = [
        "original_geometry",
        "area_sqm",
        "area_sqhm",
        "object_id",
        "content_type",
        "created_from",
        "source_of",
    ]


class OccurrenceReportGeometryInlineForm(forms.ModelForm):
    geometry = GeometryField()

    class Meta:
        model = OccurrenceReportGeometry
        fields = "__all__"


class OccurrenceReportGeometryInline(admin.StackedInline):
    model = OccurrenceReportGeometry
    form = OccurrenceReportGeometryInlineForm
    extra = 0
    verbose_name = "Occurrence Report Geometry"
    verbose_name_plural = "Occurrence Report Geometries"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "geometry",
                    ("original_geometry"),
                    (
                        "area_sqm",
                        "area_sqhm",
                    ),
                    (
                        "intersects",
                        "locked",
                    ),
                    (
                        # "copied_from",
                        "drawn_by",
                    ),
                    (
                        "object_id",
                        "content_type",
                        "created_from",
                        "source_of",
                    ),
                )
            },
        ),
    )

    readonly_fields = [
        "original_geometry",
        "area_sqm",
        "area_sqhm",
        "object_id",
        "content_type",
        "created_from",
        "source_of",
    ]


class OccurrenceGeometryInlineForm(forms.ModelForm):
    geometry = GeometryField()

    class Meta:
        model = OccurrenceGeometry
        fields = "__all__"


# class


class OccurrenceGeometryInline(nested_admin.NestedStackedInline):
    model = OccurrenceGeometry
    form = OccurrenceGeometryInlineForm
    extra = 0
    verbose_name = "Occurrence Geometry"
    verbose_name_plural = "Occurrence Geometries"

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "geometry",
                    ("original_geometry"),
                    (
                        "area_sqm",
                        "area_sqhm",
                    ),
                    (
                        "intersects",
                        "locked",
                    ),
                    (
                        # "copied_from",
                        "drawn_by",
                    ),
                    ("buffer_radius",),
                    (
                        "object_id",
                        "content_type",
                        "created_from",
                        "source_of",
                    ),
                )
            },
        ),
    )

    readonly_fields = [
        "original_geometry",
        "area_sqm",
        "area_sqhm",
        "object_id",
        "content_type",
        "created_from",
        "source_of",
    ]

    inlines = [BufferGeometryInline, OccurrenceTenureInline]


@admin.register(OccurrenceReport)
class OccurrenceReportAdmin(admin.ModelAdmin):
    inlines = [OccurrenceReportGeometryInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if hasattr(instance, "geometry"):
                geometry = instance.geometry

                instance_geometry = transform_geosgeometry_3857_to_4326(geometry)
                instance.geometry = GEOSGeometry(instance_geometry.wkt)

            instance.save()
        formset.save_m2m()


@admin.register(Occurrence)
class OccurrenceAdmin(nested_admin.NestedModelAdmin):
    inlines = [OccurrenceGeometryInline]

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()
        for instance in instances:
            if hasattr(instance, "geometry"):
                geometry = instance.geometry

                instance_geometry = transform_geosgeometry_3857_to_4326(geometry)
                instance.geometry = GEOSGeometry(instance_geometry.wkt)

            instance.save()
        formset.save_m2m()


class OccurrenceTenureAdminForm(forms.ModelForm):
    # geometry = forms.GeometryField(widget=forms.OSMWidget(attrs={"display_raw": False}))

    class Meta:
        model = OccurrenceTenure
        fields = "__all__"


@admin.register(OccurrenceTenure)
class OccurrenceTenureAdmin(nested_admin.NestedModelAdmin):
    model = OccurrenceTenure
    form = OccurrenceTenureAdminForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        "status",
                        "occurrence",
                        "significant_to_occurrence",
                        "purpose",
                        "comments",
                    ),
                )
            },
        ),
        (
            "Cadastre Spatial Identification",
            {
                "fields": (
                    ("tenure_area_id",),
                    (
                        "typename",
                        "featureid",
                    ),
                    ("tenure_area"),
                )
            },
        ),
        (
            "Cadastre Owner Information",
            {
                "fields": (
                    (
                        "owner_name",
                        "owner_count",
                    ),
                )
            },
        ),
        (
            "Occurrence Geometry",
            {
                "fields": (
                    "occurrence_geometry",
                    "geometry",
                )
            },
        ),
    )

    readonly_fields = ["typename", "featureid", "tenure_area", "geometry", "occurrence"]
    list_filter = ("status", "significant_to_occurrence", "purpose")

    def occurrence(self, obj):
        if obj.status == obj.STATUS_HISTORICAL:
            return f"{obj.occurrence.__str__()} [Historical]"
        return obj.occurrence

    def geometry(self, obj):
        if obj.status == obj.STATUS_HISTORICAL:
            geom = wkb_to_geojson(obj.historical_occurrence_geometry_ewkb)
            geom["properties"]["status"] = obj.STATUS_HISTORICAL
            geom["properties"]["occurrence_id"] = obj.occurrence.id
            return geom
        return obj.occurrence_geometry

    def tenure_area(self, obj):
        if obj.tenure_area_ewkb is None:
            return None
        return wkb_to_geojson(obj.tenure_area_ewkb)


@admin.register(OccurrenceTenurePurpose)
class OccurrenceTenurePurposeAdmin(admin.ModelAdmin):
    pass


# Each of the following models will be available to Django Admin.
admin.site.register(LandForm)
admin.site.register(RockType)
admin.site.register(SoilType)
admin.site.register(SoilColour)
admin.site.register(SoilCondition)
admin.site.register(Drainage)
admin.site.register(Intensity)
admin.site.register(ObservationMethod)
admin.site.register(PlantCountMethod)
admin.site.register(PlantCountAccuracy)
admin.site.register(CountedSubject)
admin.site.register(PlantCondition)
admin.site.register(PrimaryDetectionMethod)
admin.site.register(SecondarySign)
admin.site.register(ReproductiveState)
admin.site.register(DeathReason)
admin.site.register(AnimalHealth)
admin.site.register(IdentificationCertainty)
admin.site.register(SampleType)
admin.site.register(SampleDestination)
admin.site.register(PermitType)
admin.site.register(Datum)
admin.site.register(CoordinationSource)
admin.site.register(LocationAccuracy)
admin.site.register(WildStatus)
