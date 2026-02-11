from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
   help = "Create or update the admin superuser from env vars"

   def handle(self, *args, **options):
       User = get_user_model()

       username = os.environ.get("SUPERUSER_USERNAME", "admin")
       email = os.environ.get("SUPERUSER_EMAIL", "tip@immopros.fr")
       password = os.environ.get("SUPERUSER_PASSWORD")

       if not password:
           self.stdout.write(self.style.ERROR("Missing SUPERUSER_PASSWORD environment variable"))
           return

       user, created = User.objects.get_or_create(
           username=username,
           defaults={"email": email},
       )

       # Force update each time (important)
       user.email = email
       user.is_staff = True
       user.is_superuser = True
       user.set_password(password)
       user.save()

       if created:
           self.stdout.write(self.style.SUCCESS("✅ Superuser created"))
       else:
           self.stdout.write(self.style.SUCCESS("✅ Superuser updated (password reset)"))
