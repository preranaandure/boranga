import logging

import ledger_api_client
from django.conf import settings
from django.core.cache import cache
from django.db import models
from ledger_api_client.ledger_models import EmailUserRO
from ledger_api_client.ledger_models import EmailUserRO as EmailUser
from ledger_api_client.managed_models import SystemGroup

from boranga.settings import (
    GROUP_NAME_APPROVER,
    GROUP_NAME_ASSESSOR,
    GROUP_NAME_EDITOR,
    GROUP_NAME_OCCURRENCE_APPROVER,
    GROUP_NAME_OCCURRENCE_ASSESSOR,
)

logger = logging.getLogger(__name__)


def belongs_to(user, group_name):
    """
    Check if the user belongs to the given group.
    :param user:
    :param group_name:
    :return:
    """
    # import ipdb; ipdb.set_trace()
    belongs_to_value = cache.get(
        "User-belongs_to" + str(user.id) + "group_name:" + group_name
    )
    if belongs_to_value:
        print(
            "From Cache - User-belongs_to" + str(user.id) + "group_name:" + group_name
        )
    if belongs_to_value is None:
        belongs_to_value = False
        system_group = ledger_api_client.managed_models.SystemGroup.objects.get(
            name=group_name
        )
        if user.id in system_group.get_system_group_member_ids():
            belongs_to_value = True
        cache.set(
            "User-belongs_to" + str(user.id) + "group_name:" + group_name,
            belongs_to_value,
            3600,
        )
    return belongs_to_value

    # return user.groups.filter(name=group_name).exists()


# def is_model_backend(request):
#    # Return True if user logged in via single sign-on (i.e. an internal)
#    return 'ModelBackend' in request.session.get('_auth_user_backend')
#
# def is_email_auth_backend(request):
#    # Return True if user logged in via social_auth (i.e. an external user signing in with a login-token)
#    return 'EmailAuth' in request.session.get('_auth_user_backend')


def is_boranga_admin(request):
    # import ipdb; ipdb.set_trace()
    # logger.info('settings.ADMIN_GROUP: {}'.format(settings.ADMIN_GROUP))
    return request.user.is_authenticated and (
        belongs_to(request.user, settings.ADMIN_GROUP) or request.user.is_superuser
    )


def is_django_admin(request):
    return request.user.is_authenticated and (
        belongs_to(request.user, settings.DJANGO_ADMIN_GROUP)
        or request.user.is_superuser
    )


def is_assessor(user_id):
    if isinstance(user_id, EmailUser) or isinstance(user_id, EmailUserRO):
        user_id = user_id.id
    assessor_group = SystemGroup.objects.get(name=GROUP_NAME_ASSESSOR)
    return True if user_id in assessor_group.get_system_group_member_ids() else False


def is_approver(user_id):
    if isinstance(user_id, EmailUser) or isinstance(user_id, EmailUserRO):
        user_id = user_id.id
    assessor_group = SystemGroup.objects.get(name=GROUP_NAME_APPROVER)
    return True if user_id in assessor_group.get_system_group_member_ids() else False


def is_conservation_status_referee(request, cs_proposal=None):
    from boranga.components.conservation_status.models import ConservationStatusReferral

    qs = ConservationStatusReferral.objects.filter(referral=request.user.id)
    if cs_proposal:
        qs = qs.filter(conservation_status=cs_proposal)

    return qs.exists()


def is_conservation_status_editor(user_id):
    if isinstance(user_id, EmailUser) or isinstance(user_id, EmailUserRO):
        user_id = user_id.id
    assessor_group = SystemGroup.objects.get(name=GROUP_NAME_EDITOR)
    return True if user_id in assessor_group.get_system_group_member_ids() else False


def is_occurrence_assessor(user_id):
    if isinstance(user_id, EmailUser) or isinstance(user_id, EmailUserRO):
        user_id = user_id.id
    assessor_group = SystemGroup.objects.get(name=GROUP_NAME_OCCURRENCE_ASSESSOR)
    return True if user_id in assessor_group.get_system_group_member_ids() else False


def is_occurrence_approver(user_id):
    if isinstance(user_id, EmailUser) or isinstance(user_id, EmailUserRO):
        user_id = user_id.id
    assessor_group = SystemGroup.objects.get(name=GROUP_NAME_OCCURRENCE_APPROVER)
    return True if user_id in assessor_group.get_system_group_member_ids() else False


def in_dbca_domain(request):
    user = request.user
    domain = user.email.split("@")[1]
    if domain in settings.DEPT_DOMAINS:
        if not user.is_staff:
            # hack to reset department user to is_staff==True, if the user logged in externally
            # (external departmentUser login defaults to is_staff=False)
            user.is_staff = True
            user.save()
        return True
    return False


def email_in_dept_domains(email):
    return email.split("@")[1] in settings.DEPT_DOMAINS


def is_in_organisation_contacts(request, organisation):
    return request.user.email in organisation.contacts.all().values_list(
        "email", flat=True
    )


def is_departmentUser(request):
    # return request.user.is_authenticated and is_model_backend(request) and in_dbca_domain(request)
    return request.user.is_authenticated and in_dbca_domain(request)


def is_customer(request):
    return request.user.is_authenticated and not request.user.is_staff


def is_internal(request):
    return is_departmentUser(request)


def get_all_officers():
    return EmailUser.objects.filter(groups__name=settings.ADMIN_GROUP)


def get_instance_identifier(instance):
    """Checks the instance for the attributes specified in settings"""
    for field in settings.ACTION_LOGGING_IDENTIFIER_FIELDS:
        if hasattr(instance, field):
            return getattr(instance, field)
    raise AttributeError(
        f"Model instance has no valid identifier to use for logging. Tried: {settings.ACTION_LOGGING_IDENTIFIER_FIELDS}"
    )


def clone_model(
    source_model_class: models.base.ModelBase,
    target_model_class: models.base.ModelBase,
    source_model: models.Model,
    save: bool = False,
) -> models.Model:
    """
    Copies field values from source_model to a new instance of target_model_class.

    Will complain if:
        - source_model is not an instance of source_model_class.
        - the new instance of target_model_class does not contain a field that is in source_model.

    Returns None if source_model is None so caller must check for existence of return value.

    Pass save=True to save the new instance to the database automatically after copying the field values.
    """
    logger.debug(f"Save: {save}")
    if source_model is None:
        return None

    if not isinstance(source_model, source_model_class):
        raise ValueError(
            f"source_model is not an instance of {source_model_class.__name__}"
        )

    target_model = target_model_class()

    try:
        for field in source_model._meta.fields:
            if field.primary_key:
                continue

            setattr(target_model, field.name, getattr(source_model, field.name))
    except AttributeError as e:
        logger.error(
            f"Error copying field values from {source_model} to {target_model}: {e}"
        )
    if save:
        target_model.save()

    return target_model
