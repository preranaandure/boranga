from __future__ import unicode_literals
import os

from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
#from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
#from ledger.accounts.models import EmailUser, Document, RevisionedMixin
from ledger_api_client.ledger_models import EmailUserRO as EmailUser, BaseAddress#, RevisionedMixin
#from django.contrib.postgres.fields.jsonb import JSONField
from django.db.models import JSONField
from django.conf import settings
from django.core.files.storage import FileSystemStorage
private_storage = FileSystemStorage(location=settings.BASE_DIR+"/private-media/", base_url='/private-media/')

## TODO: remove ledger models

##@python_2_unicode_compatible
#class Organisation(models.Model):
#    """This model represents the details of a company or other organisation.
#    Management of these objects will be delegated to 0+ EmailUsers.
#    """
#    name = models.CharField(max_length=128, unique=True)
#    abn = models.CharField(max_length=50, null=True, blank=True, verbose_name='ABN')
#    # TODO: business logic related to identification file upload/changes.
#    identification = models.FileField(upload_to='%Y/%m/%d', null=True, blank=True)
#    postal_address = models.ForeignKey('OrganisationAddress', related_name='org_postal_address', blank=True, null=True, on_delete=models.SET_NULL)
#    billing_address = models.ForeignKey('OrganisationAddress', related_name='org_billing_address', blank=True, null=True, on_delete=models.SET_NULL)
#    email = models.EmailField(blank=True, null=True,)
#    trading_name = models.CharField(max_length=256, null=True, blank=True)
#
#    def upload_identification(self, request):
#        with transaction.atomic():
#            self.identification = request.data.dict()['identification']
#            self.save()
#
#    def __str__(self):
#        return self.name
#
#    class Meta:
#        #abstract = True
#        managed = False
#
#class OrganisationAddress(BaseAddress):
#    organisation = models.ForeignKey(Organisation, null=True,blank=True, related_name='adresses', on_delete=models.CASCADE)
#    class Meta:
#        verbose_name_plural = 'organisation addresses'
#        unique_together = ('organisation','hash')
#
#    class Meta:
#        #abstract = True
#        managed = False

#####

class RevisionedMixin(models.Model):
    """
    A model tracked by reversion through the save method.
    """
    def save(self, **kwargs):
        from reversion import revisions
        if kwargs.pop('no_revision', False):
            super(RevisionedMixin, self).save(**kwargs)
        else:
            with revisions.create_revision():
                if 'version_user' in kwargs:
                    revisions.set_user(kwargs.pop('version_user', None))
                if 'version_comment' in kwargs:
                    revisions.set_comment(kwargs.pop('version_comment', ''))
                super(RevisionedMixin, self).save(**kwargs)

    @property
    def created_date(self):
        #return revisions.get_for_object(self).last().revision.date_created
        return Version.objects.get_for_object(self).last().revision.date_created

    @property
    def modified_date(self):
        #return revisions.get_for_object(self).first().revision.date_created
        return Version.objects.get_for_object(self).first().revision.date_created

    class Meta:
        abstract = True


# #@python_2_unicode_compatible
# class RequiredDocument(models.Model):
#     question = models.TextField(blank=False)

#     class Meta:
#         app_label = 'boranga'

#     def __str__(self):
#         return self.question

#@python_2_unicode_compatible
# class ApplicationType(models.Model):
#     """
#     for park in Park.objects.all().order_by('id'):
#         ParkPrice.objects.create(park=park, adult=10.0, child=7.50, senior=5.00)
#     """
#     #TCLASS = 'T Class'
#     TCLASS = 'Commercial operations'
#     ECLASS = 'E Class'
#     FILMING = 'Filming'
#     EVENT = 'Event'
#     name = models.CharField(max_length=64, unique=True)
#     order = models.PositiveSmallIntegerField(default=0)
#     visible = models.BooleanField(default=True)

#     application_fee = models.DecimalField('Application Fee', max_digits=6, decimal_places=2, null=True)
#     oracle_code_application = models.CharField(max_length=50)
#     oracle_code_licence = models.CharField(max_length=50)
#     is_gst_exempt = models.BooleanField(default=True)

#     class Meta:
#         ordering = ['order', 'name']
#         app_label = 'boranga'

#     def __str__(self):
#         return self.name


#@python_2_unicode_compatible
# class OracleCode(models.Model):
#     CODE_TYPE_CHOICES = (
#         (ApplicationType.TCLASS, ApplicationType.TCLASS),
#         (ApplicationType.FILMING, ApplicationType.FILMING),
#         (ApplicationType.EVENT, ApplicationType.EVENT),
#     )
#     code_type = models.CharField('Application Type', max_length=64, choices=CODE_TYPE_CHOICES,
#                                         default=CODE_TYPE_CHOICES[0][0])
#     code = models.CharField(max_length=50, blank=True)
#     archive_date = models.DateField(null=True, blank=True)

#     class Meta:
#         app_label = 'boranga'

#     def __str__(self):
#         return '{} - {}'.format(self.code_type, self.code)


#@python_2_unicode_compatible
# class Question(models.Model):
#     CORRECT_ANSWER_CHOICES = (
#         ('answer_one', 'Answer one'), ('answer_two', 'Answer two'), ('answer_three', 'Answer three'),
#         ('answer_four', 'Answer four'))
#     question_text = models.TextField(blank=False)
#     answer_one = models.CharField(max_length=200, blank=True)
#     answer_two = models.CharField(max_length=200, blank=True)
#     answer_three = models.CharField(max_length=200, blank=True)
#     answer_four = models.CharField(max_length=200, blank=True)
#     #answer_five = models.CharField(max_length=200, blank=True)
#     correct_answer = models.CharField('Correct Answer', max_length=40, choices=CORRECT_ANSWER_CHOICES,
#                                        default=CORRECT_ANSWER_CHOICES[0][0])
#     application_type = models.ForeignKey(ApplicationType, null=True, blank=True, on_delete=models.SET_NULL)

#     class Meta:
#         #ordering = ['name']
#         app_label = 'boranga'

#     def __str__(self):
#         return self.question_text

#     @property
#     def correct_answer_value(self):
#         return getattr(self, self.correct_answer)


#@python_2_unicode_compatible
class UserAction(models.Model):
    #who = models.ForeignKey(EmailUser, null=True, blank=True, on_delete=models.SET_NULL)
    who = models.IntegerField() #EmailUserRO
    when = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    what = models.TextField(blank=False)

    def __str__(self):
        return "{what} ({who} at {when})".format(
            what=self.what,
            who=self.who,
            when=self.when
        )

    class Meta:
        abstract = True
        app_label = 'boranga'


class CommunicationsLogEntry(models.Model):
    TYPE_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone Call'),
        ('mail', 'Mail'),
        ('person', 'In Person'),
        ('onhold', 'On Hold'),
        ('onhold_remove', 'Remove On Hold'),
        ('with_qaofficer', 'With QA Officer'),
        ('with_qaofficer_completed', 'QA Officer Completed'),
        ('referral_complete','Referral Completed'),
    ]
    DEFAULT_TYPE = TYPE_CHOICES[0][0]

    #to = models.CharField(max_length=200, blank=True, verbose_name="To")
    to = models.TextField(blank=True, verbose_name="To")
    fromm = models.CharField(max_length=200, blank=True, verbose_name="From")
    #cc = models.CharField(max_length=200, blank=True, verbose_name="cc")
    cc = models.TextField(blank=True, verbose_name="cc")

    type = models.CharField(max_length=35, choices=TYPE_CHOICES, default=DEFAULT_TYPE)
    reference = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=200, blank=True, verbose_name="Subject / Description")
    text = models.TextField(blank=True)

    #customer = models.ForeignKey(EmailUser, null=True, related_name='+', on_delete=models.SET_NULL)
    customer = models.IntegerField(null=True) #EmailUserRO
    #staff = models.ForeignKey(EmailUser, null=True, related_name='+', on_delete=models.SET_NULL)
    staff = models.IntegerField() #EmailUserRO

    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        app_label = 'boranga'


#@python_2_unicode_compatible
class Document(models.Model):
    name = models.CharField(max_length=255, blank=True,
                            verbose_name='name', help_text='')
    description = models.TextField(blank=True,
                                   verbose_name='description', help_text='')
    uploaded_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'boranga'
        abstract = True

    @property
    def path(self):
        #return self.file.path
        #return self._file.path
        #comment above line to fix the error "The '_file' attribute has no file associated with it." when adding comms log entry.
        if self._file:
            return self._file.path
        else:
            return ''

    @property
    def filename(self):
        return os.path.basename(self.path)

    def __str__(self):
        return self.name or self.filename

class GlobalSettings(models.Model):
    keys = (
        ('credit_facility_link', 'Credit Facility Link'),
        ('deed_poll', 'Deed poll'),
        ('deed_poll_filming', 'Deed poll Filming'),
        ('deed_poll_event', 'Deed poll Event'),
        ('online_training_document', 'Online Training Document'),
        ('park_finder_link', 'Park Finder Link'),
        ('fees_and_charges', 'Fees and charges link'),
        ('event_fees_and_charges', 'Event Fees and charges link'),
        ('commercial_filming_handbook', 'Commercial Filming Handbook link'),
        ('park_stay_link', 'Park Stay Link'),
        ('event_traffic_code_of_practice', 'Event traffic code of practice'),
        ('trail_section_map', 'Trail section map'),
        ('dwer_application_form', 'DWER Application Form'),

    )
    key = models.CharField(max_length=255, choices=keys, blank=False, null=False,)
    value = models.CharField(max_length=255)

    class Meta:
        app_label = 'boranga'
        verbose_name_plural = "Global Settings"


#@python_2_unicode_compatible
class SystemMaintenance(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def duration(self):
        """ Duration of system maintenance (in mins) """
        return int( (self.end_date - self.start_date).total_seconds()/60.) if self.end_date and self.start_date else ''
        #return (datetime.now(tz=tz) - self.start_date).total_seconds()/60.
    duration.short_description = 'Duration (mins)'

    class Meta:
        app_label = 'boranga'
        verbose_name_plural = "System maintenance"

    def __str__(self):
        return 'System Maintenance: {} ({}) - starting {}, ending {}'.format(self.name, self.description, self.start_date, self.end_date)

class UserSystemSettings(models.Model):
    #user = models.OneToOneField(EmailUser, related_name='system_settings', on_delete=models.CASCADE)
    user = models.IntegerField(unique=True) #EmailUserRO
    event_training_completed = models.BooleanField(default=False)
    event_training_date= models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'boranga'
        verbose_name_plural = "User System Settings"


#import reversion
#reversion.register(Region, follow=['districts'])
#reversion.register(District, follow=['parks'])
##reversion.register(AccessType)
#reversion.register(AccessType, follow=['park_set', 'proposalparkaccess_set', 'vehicles'])
#reversion.register(ActivityType)
#reversion.register(ActivityCategory, follow=['activities'])
##reversion.register(Activity, follow=['park_set', 'zone_set', 'trail_set', 'requireddocument_set'])
#reversion.register(Activity, follow=['park_set', 'zone_set', 'trail_set', 'requireddocument_set', 'proposalparkactivity_set','proposalparkzoneactivity_set', 'proposaltrailsectionactivity_set'])
#reversion.register(Park, follow=['zones', 'requireddocument_set', 'proposals'])
#reversion.register(Zone, follow=['proposal_zones'])
#reversion.register(Trail, follow=['sections', 'proposals'])
#reversion.register(Section, follow=['proposal_trails'])
#reversion.register(RequiredDocument)
#reversion.register(ApplicationType, follow=['tenure_app_types', 'helppage_set'])
#reversion.register(ActivityMatrix)
#reversion.register(Tenure)
#reversion.register(Question)
#reversion.register(UserAction)
#reversion.register(CommunicationsLogEntry)
#reversion.register(Document)
#reversion.register(SystemMaintenance)

