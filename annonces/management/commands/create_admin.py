from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):
   help = "Create initial superuser if not exists"

   def handle(self, *args, **kwargs):
       User = get_user_model()

       username = os.environ.get("SUPERUSER_USERNAME")
       email = os.environ.get("SUPERUSER_EMAIL")
       password = os.environ.get("SUPERUSER_PASSWORD")

       if not username or not email or not password:
           self.stdout.write(self.style.ERROR("Missing SUPERUSER environment variables"))
           return

       if User.objects.filter(username=username).exists():
           self.stdout.write("Superuser already exists")
           return

       User.objects.create_superuser(
           username=username,
           email=email,
           password=password
       )

       self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
