from django.shortcuts import render, get_object_or_404, redirect
from .models import Annonce
from .forms import AnnonceForm

def home(request):
    # Home = liste des dernières annonces
    annonces = Annonce.objects.order_by('-id')[:50]
    return render(request, "annonces/home.html", {"annonces": annonces})

def annonce_detail(request, pk: int):
    annonce = get_object_or_404(Annonce, pk=pk)
    return render(request, "annonces/detail.html", {"annonce": annonce})

def annonce_create(request):
    if request.method == "POST":
        form = AnnonceForm(request.POST)
        if form.is_valid():
            annonce = form.save()
            return redirect("annonce_detail", pk=annonce.pk)
    else:
        form = AnnonceForm()
    return render(request, "annonces/create.html", {"form": form})


from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings
from django.contrib.auth import get_user_model

def setup_admin(request):
    """Crée un superuser SANS terminal (usage ponctuel).

    Utilisation:
    /setup-admin/?token=XXX

    Variables d'environnement à définir sur l'hébergeur:
    - SETUP_TOKEN
    - ADMIN_USERNAME (optionnel, défaut: admin)
    - ADMIN_EMAIL (optionnel)
    - ADMIN_PASSWORD
    """
    expected = os.environ.get("SETUP_TOKEN")
    token = request.GET.get("token")
    if not expected or token != expected:
        return HttpResponseForbidden("Forbidden")

    User = get_user_model()
    if User.objects.filter(is_superuser=True).exists():
        return HttpResponse("Superuser already exists.")

    username = os.environ.get("ADMIN_USERNAME", "admin")
    email = os.environ.get("ADMIN_EMAIL", "")
    password = os.environ.get("ADMIN_PASSWORD")
    if not password:
        return HttpResponse("Missing ADMIN_PASSWORD env var.", status=400)

    User.objects.create_superuser(username=username, email=email, password=password)
    return HttpResponse("Superuser created. You can now login at /admin/.")
