from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Force create superuser (reset if needed)"

    def handle(self, *args, **options):
        User = get_user_model()

        # Supprime tous les utilisateurs existants
        User.objects.all().delete()

        # Crée un nouvel admin
        User.objects.create_superuser(
            username="admin",
            email="tip@immopros.fr",
            password="Admin2026!"
        )

        self.stdout.write(self.style.SUCCESS("Superuser recreated successfully"))
