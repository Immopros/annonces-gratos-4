from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Create initial admin user if none exists"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        username = os.environ.get("SUPERUSER_USERNAME", "admin")
        email = os.environ.get("SUPERUSER_EMAIL", "tip@immopros.fr")
        password = os.environ.get("SUPERUSER_PASSWORD", "Admin123!")

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("Superuser already exists")
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )

        self.stdout.write("✅ Superuser created")
