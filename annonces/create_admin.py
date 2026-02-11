from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Create initial superuser if none exists"

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("Superuser already exists")
            return

        User.objects.create_superuser(
            username="admin",
            email="tip@immopros.fr",
            password="Admin-Olive350@"
        )

        self.stdout.write("✅ Superuser created")
