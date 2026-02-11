from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Create or update the initial superuser from environment variables"

    def handle(self, *args, **options):
        User = get_user_model()

        username = getattr(settings, "SUPERUSER_USERNAME", None) or getattr(settings, "DJANGO_SUPERUSER_USERNAME", None)
        email = getattr(settings, "SUPERUSER_EMAIL", None) or getattr(settings, "DJANGO_SUPERUSER_EMAIL", None)
        password = getattr(settings, "SUPERUSER_PASSWORD", None) or getattr(settings, "DJANGO_SUPERUSER_PASSWORD", None)

        if not username or not password:
            self.stdout.write(self.style.WARNING("SUPERUSER_USERNAME / SUPERUSER_PASSWORD manquants."))
            return

        user, created = User.objects.get_or_create(username=username, defaults={"email": email or ""})

        # Toujours forcer les droits + le mot de passe (même si l'user existe déjà)
        user.is_staff = True
        user.is_superuser = True
        if email:
            user.email = email
        user.set_password(password)
        user.save()

        msg = "créé" if created else "mis à jour"
        self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' {msg}"))
