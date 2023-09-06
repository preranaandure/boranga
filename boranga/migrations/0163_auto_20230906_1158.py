# Generated by Django 3.2.20 on 2023-09-06 03:58

import boranga.components.approvals.models
import boranga.components.compliances.models
import boranga.components.conservation_status.models
import boranga.components.meetings.models
import boranga.components.organisations.models
import boranga.components.proposals.models
import boranga.components.species_and_communities.models
import django.core.files.storage
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boranga', '0162_merge_0160_auto_20230824_1549_0161_auto_20230825_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committeemeeting',
            name='attendees',
        ),
        migrations.RemoveField(
            model_name='committeemeeting',
            name='species',
        ),
        migrations.DeleteModel(
            name='NameAuthority',
        ),
        migrations.DeleteModel(
            name='ScientificName',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.RemoveField(
            model_name='speciesattributes',
            name='species',
        ),
        migrations.RemoveField(
            model_name='taxonomy',
            name='family',
        ),
        migrations.RemoveField(
            model_name='taxonomy',
            name='phylogenetic_group',
        ),
        migrations.AlterField(
            model_name='approvaldocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.approvals.models.update_approval_doc_filename),
        ),
        migrations.AlterField(
            model_name='approvallogdocument',
            name='_file',
            field=models.FileField(max_length=512, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.approvals.models.update_approval_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='communitydocument',
            name='_file',
            field=models.FileField(default='None', max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.species_and_communities.models.update_community_doc_filename),
        ),
        migrations.AlterField(
            model_name='communitylogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.species_and_communities.models.update_community_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.compliances.models.update_proposal_complaince_filename),
        ),
        migrations.AlterField(
            model_name='compliancelogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.compliances.models.update_compliance_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='conservationstatusamendmentrequestdocument',
            name='_file',
            field=models.FileField(max_length=500, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.conservation_status.models.update_conservation_status_amendment_request_doc_filename),
        ),
        migrations.AlterField(
            model_name='conservationstatusdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.conservation_status.models.update_conservation_status_doc_filename),
        ),
        migrations.AlterField(
            model_name='conservationstatuslogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.conservation_status.models.update_conservation_status_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='conservationstatusreferraldocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.conservation_status.models.update_referral_doc_filename),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='completely_degraded',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='degraded',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='excellent',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='good',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='pristine',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='habitatcondition',
            name='very_good',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='meetinglogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.meetings.models.update_meeting_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='minutes',
            name='_file',
            field=models.FileField(default='None', max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.meetings.models.update_meeting_doc_filename),
        ),
        migrations.AlterField(
            model_name='onholddocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_onhold_doc_filename),
        ),
        migrations.AlterField(
            model_name='organisationlogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.organisations.models.update_organisation_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='organisationrequest',
            name='identification',
            field=models.FileField(blank=True, max_length=512, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to='organisation/requests/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='organisationrequestlogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.organisations.models.update_organisation_request_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='proposaldocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_proposal_doc_filename),
        ),
        migrations.AlterField(
            model_name='proposallogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_proposal_comms_log_filename),
        ),
        migrations.AlterField(
            model_name='proposalrequireddocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_proposal_required_doc_filename),
        ),
        migrations.AlterField(
            model_name='qaofficerdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_qaofficer_doc_filename),
        ),
        migrations.AlterField(
            model_name='requirementdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.proposals.models.update_requirement_doc_filename),
        ),
        migrations.AlterField(
            model_name='speciesdocument',
            name='_file',
            field=models.FileField(default='None', max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.species_and_communities.models.update_species_doc_filename),
        ),
        migrations.AlterField(
            model_name='specieslogdocument',
            name='_file',
            field=models.FileField(max_length=512, storage=django.core.files.storage.FileSystemStorage(base_url='/private-media/', location='/data/data/projects/boranga/private-media/'), upload_to=boranga.components.species_and_communities.models.update_species_comms_log_filename),
        ),
        migrations.DeleteModel(
            name='CommitteeMeeting',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Family',
        ),
        migrations.DeleteModel(
            name='PhylogeneticGroup',
        ),
        migrations.DeleteModel(
            name='SpeciesAttributes',
        ),
    ]
