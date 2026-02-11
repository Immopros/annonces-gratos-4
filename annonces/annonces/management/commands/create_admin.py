from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

class Command(BaseCommand):
  def handle(self, *args, **kwargs):
      User = get_user_model()

      username = settings.SUPERUSER_USERNAME
      email = settings.SUPERUSER_EMAIL
      password = settings.SUPERUSER_PASSWORD

      User.objects.filter(username=username).delete()

      User.objects.create_superuser(
          username=username,
          email=email,
          password=password
      )

      print("Superuser recréé correctement")

