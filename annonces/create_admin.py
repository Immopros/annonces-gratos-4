import os
from django.contrib.auth import get_user_model

def create_superuser():
    username = os.environ.get("SUPERUSER_USERNAME")
    email = os.environ.get("SUPERUSER_EMAIL", "")
    password = os.environ.get("SUPERUSER_PASSWORD")

    if not username or not password:
        return

    User = get_user_model()
    if User.objects.filter(username=username).exists():
        return

    User.objects.create_superuser(username=username, email=email, password=password)
