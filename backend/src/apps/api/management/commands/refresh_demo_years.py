import datetime
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.core.modules.terms.models import Year
from apps.core.modules.users.models import User


class Command(BaseCommand):
    help = "Move the public demo's academic years to the current school cycle."

    @transaction.atomic
    def handle(self, *args, **options):
        email = os.getenv("DEMO_READ_ONLY_EMAIL", "").strip().lower()
        if not email:
            self.stdout.write("DEMO_READ_ONLY_EMAIL is not set; demo years unchanged.")
            return

        try:
            user = User.objects.select_related("school").get(email__iexact=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f"Demo account {email} was not found."))
            return

        if user.school_id is None:
            self.stdout.write(self.style.WARNING("Demo account has no school; years unchanged."))
            return

        years = list(Year.objects.filter(school=user.school).order_by("id"))
        if not years:
            self.stdout.write(self.style.WARNING("Demo school has no academic years."))
            return

        today = datetime.date.today()
        current_start = today.year if today.month >= 8 else today.year - 1

        for year in years:
            Year.objects.filter(pk=year.pk).update(name=f"demo-year-{year.pk}")

        for index, year in enumerate(years):
            start_year = current_start - (len(years) - 1 - index)
            Year.objects.filter(pk=year.pk).update(
                name=f"{start_year}-{start_year + 1}",
                is_active=True,
                is_opened_to_marks=index == len(years) - 1,
            )

            for term in year.terms.all():
                from_year = start_year if term.from_date.month >= 8 else start_year + 1
                to_year = start_year if term.to_date.month >= 8 else start_year + 1
                year.terms.filter(pk=term.pk).update(
                    from_date=term.from_date.replace(year=from_year),
                    to_date=term.to_date.replace(year=to_year),
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Updated demo years through {current_start}-{current_start + 1}."
            )
        )
