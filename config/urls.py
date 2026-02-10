from django.contrib import admin
from django.urls import path, include
from annonces.views import setup_admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("setup-admin/<str:token>/", setup_admin),
    path("", include("annonces.urls")),
]
