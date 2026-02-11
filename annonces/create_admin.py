from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Create or update the initial superuser"

    def handle(self, *args, **options):
        User = get_user_model()

        username = getattr(settings, "SUPERUSER_USERNAME", None)
        email = getattr(settings, "SUPERUSER_EMAIL", None)
        password = getattr(settings, "SUPERUSER_PASSWORD", None)

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR(
                "Missing SUPERUSER_USERNAME / SUPERUSER_EMAIL / SUPERUSER_PASSWORD"
            ))
            return

        user, created = User.objects.get_or_create(
            username=username,
            defaults={"email": email}
        )

        # Force update every time
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS("✅ Superuser created"))
        else:
            self.stdout.write(self.style.SUCCESS("✅ Superuser updated"))
