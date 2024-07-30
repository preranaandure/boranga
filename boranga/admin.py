from copy import deepcopy

from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.gis import admin
from django.forms import ValidationError
from ledger_api_client.admin import SystemGroupAdmin, SystemGroupPermissionInline
from ledger_api_client.ledger_models import EmailUserRO as EmailUser
from ledger_api_client.managed_models import SystemGroup

from boranga import helpers as boranga_helpers
from boranga.components.main.models import ArchivableManager, ArchivableModel


class DeleteProtectedModelAdmin(admin.ModelAdmin):
    """Stops regular users from deleting objects in the admin but still allow superusers to do so."""

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions and not request.user.is_superuser:
            del actions["delete_selected"]
        return actions

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.action(description="Mark as archived")
def archive(modeladmin, request, queryset):
    queryset.update(archived=True)


@admin.action(description="Mark as unarchived")
def unarchive(modeladmin, request, queryset):
    queryset.update(archived=False)


class ArchivableModelAdminMixin:
    actions = [archive, unarchive]
    list_filter = ("archived",)
    search_fields = ("id",)
    ordering = ("id",)

    def __init__(self, model, admin_site) -> None:
        super().__init__(model, admin_site)

        if not hasattr(self, "model"):
            raise AttributeError("Please set the model attribute on the admin class.")

        if not issubclass(self.model, ArchivableModel):
            raise AttributeError("The model must be a sub class of ArchivableModel.")

        if not isinstance(self.model.objects, ArchivableManager):
            raise AttributeError(
                "The model manager must be an instance of ArchivableManager."
            )

    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if type(list_display) is tuple:
            list_display = list(list_display)
        return list_display + ["achived_list_view_display"]

    def achived_list_view_display(self, obj):
        return "Yes" if obj.archived else "No"

    achived_list_view_display.short_description = "Archived"

    def get_queryset(self, request):
        return self.model.objects.all_with_archived()


admin.site.index_template = "admin-index.html"
admin.autodiscover()


@admin.register(EmailUser)
class EmailUserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    ordering = ("email",)
    search_fields = ("id", "email", "first_name", "last_name")

    def has_change_permission(self, request, obj=None):
        if obj is None:  # and obj.status > 1:
            return True
        return None

    def has_delete_permission(self, request, obj=None):
        return None


class CustomSystemGroupPermissionInlineForm(SystemGroupPermissionInline.form):
    def clean(self):
        cleaned_data = super().clean()
        system_group = cleaned_data.get("system_group")
        emailuser = cleaned_data.get("emailuser")
        if system_group.name in settings.INTERNAL_GROUPS:
            if not emailuser.is_staff:
                raise ValidationError(
                    "Only internal users can be added to internal groups."
                )
        else:
            if emailuser.is_staff:
                raise ValidationError(
                    "Only external users can be added to external groups."
                )


class CustomSystemGroupPermissionInline(SystemGroupPermissionInline):
    form = CustomSystemGroupPermissionInlineForm


class CustomSystemGroupAdmin(SystemGroupAdmin):
    """
    Overriding the SystemGroupAdmin from ledger.accounts.admin,
    to remove ledger_permissions selection field for DjangoAdmin SystemGroup on Admin page
    """

    inlines = [CustomSystemGroupPermissionInline]
    filter_horizontal = ("permissions",)

    def get_fieldsets(self, request, obj=None):
        """Remove the ledger_permissions checkbox from the Admin page, if user is DjangoAdmin and NOT superuser"""
        fieldsets = super(SystemGroupAdmin, self).get_fieldsets(request, obj)
        if not obj:
            return fieldsets
        if request.user.is_superuser:
            return fieldsets
        elif boranga_helpers.is_django_admin(request):
            fieldsets = deepcopy(fieldsets)
            for fieldset in fieldsets:
                if "permissions" in fieldset[1]["fields"]:
                    if type(fieldset[1]["fields"]) is tuple:
                        fieldset[1]["fields"] = list(fieldset[1]["fields"])
                    fieldset[1]["fields"].remove("permissions")

        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        elif boranga_helpers.is_django_admin(request):
            return ["name"]  # make fields readonly when editing an existing object


admin.site.unregister(Group)
admin.site.unregister(SystemGroup)
admin.site.register(SystemGroup, CustomSystemGroupAdmin)
