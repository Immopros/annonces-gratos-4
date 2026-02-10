from django.urls import path
from .views import home, annonce_detail, annonce_create

urlpatterns = [
    path("", home, name="home"),
    path("annonces/nouvelle/", annonce_create, name="annonce_create"),
    path("annonces/<int:pk>/", annonce_detail, name="annonce_detail"),
]
