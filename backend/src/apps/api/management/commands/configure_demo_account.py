import os

from django.core.management.base import BaseCommand

from apps.core.modules.grades.models import Grade
from apps.core.modules.schools.models import School
from apps.core.modules.users.models import User


class Command(BaseCommand):
    help = "Restrict the configured public demo account to application-only access."

    def handle(self, *args, **options):
        email = os.getenv("DEMO_READ_ONLY_EMAIL", "").strip().lower()
        if not email:
            self.stdout.write("DEMO_READ_ONLY_EMAIL is not set; no account changed.")
            return

        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING(f"Demo account {email} was not found."))
            return

        user.role = User.Role.MANAGER
        user.is_staff = False
        user.is_superuser = False
        update_fields = ["role", "is_staff", "is_superuser"]

        if user.school_id is None:
            school = School.objects.order_by("id").first()
            if school:
                user.school = school
                update_fields.append("school")

        user.save(update_fields=update_fields)

        for number in range(1, 12):
            Grade.objects.update_or_create(
                school=user.school,
                name=f"{number} grade",
                defaults={"is_active": True},
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Configured {email} as a read-only demo account with grades 1-11."
            )
        )
