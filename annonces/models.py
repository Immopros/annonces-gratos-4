from django.db import models

CATEGORIES = [
    ("voitures", "Voitures"),
    ("motos", "Motos"),
    ("immobilier", "Immobilier"),
    ("commerces", "commerces"),
    ("emploi", "Emploi"),
    ("multimedia", "Multimédia"),
    ("maison", "Maison"),
    ("jouets", "jouets"),
    ("mode", "Mode"),
    ("loisirs", "Loisirs"),
    ("services", "Services"),
    ("divers", "Divers"),
]
from django.db import models

CATEGORIES = [
    ("voitures", "Voitures"),
    ...
]

class Annonce(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ville = models.CharField(max_length=120, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORIES,
        default="divers"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
        
