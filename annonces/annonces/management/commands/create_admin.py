import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or update an admin user from environment variables"

    def handle(self, *args, **options):
        username = os.environ.get("SUPERUSER_USERNAME", "admin")
        email = os.environ.get("SUPERUSER_EMAIL", "")
        password = os.environ.get("SUPERUSER_PASSWORD", "")

        if not password:
            self.stdout.write(self.style.WARNING("SUPERUSER_PASSWORD missing → skip admin creation"))
            return

        User = get_user_model()

        user, created = User.objects.get_or_create(username=username, defaults={"email": email})

        # Toujours s'assurer qu'il est admin
        user.is_staff = True
        user.is_superuser = True

        if email:
            user.email = email

        # IMPORTANT: on force le password (comme ça tu peux le changer via Render)
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' created/updated"))
        else:
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' updated (password refreshed)"))

