from django.urls import path
from .views import home, annonce_detail, annonce_create, setup_admin

urlpatterns = [
    path('', home, name='home'),
    path('setup-admin/', setup_admin, name='setup_admin'),
    path('annonces/<int:pk>/', annonce_detail, name='annonce_detail'),
    path('annonces/nouvelle/', annonce_create, name='annonce_create'),
]
from .views import setup_admin
