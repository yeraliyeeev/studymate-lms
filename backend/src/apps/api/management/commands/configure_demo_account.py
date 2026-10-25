import os

from django.core.management.base import BaseCommand

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
        user.save(update_fields=["role", "is_staff", "is_superuser"])

        self.stdout.write(
            self.style.SUCCESS(f"Configured {email} as a read-only demo account.")
        )
