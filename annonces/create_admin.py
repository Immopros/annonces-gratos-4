from django.contrib.auth import get_user_model
from django.conf import settings

def create_superuser():
    User = get_user_model()

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username="admin",
            email="admin@annoncesgratos.fr",
            password="Admin12345!"
        )
        print("✅ Superuser créé automatiquement")
