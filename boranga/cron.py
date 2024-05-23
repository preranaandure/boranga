import logging

import django_cron
from django.core import management

log = logging.getLogger(__name__)


class CronJobFetchNomosTaxonDataDaily(django_cron.CronJobBase):
    RUN_ON_DAYS = [0, 1, 2, 3, 4, 5, 6]
    RUN_AT_TIMES = ["20:00"]
    schedule = django_cron.Schedule(run_on_days=RUN_ON_DAYS, run_at_times=RUN_AT_TIMES)
    code = "boranga.fetch_nomos_data"

    def do(self) -> None:
        log.info("Fetch Nomos Taxon Data cron job triggered, running...")
        management.call_command("fetch_nomos_blob_data")
        return "Job Completed Successfully"


class CronJobDelistExpiredConservationStatus(django_cron.CronJobBase):
    RUN_ON_DAYS = [0, 1, 2, 3, 4, 5, 6]
    RUN_AT_TIMES = ["03:00"]
    schedule = django_cron.Schedule(run_on_days=RUN_ON_DAYS, run_at_times=RUN_AT_TIMES)
    code = "boranga.delist_expired_conservation_status"

    def do(self) -> None:
        management.call_command("conservation_status_delist_expired")
