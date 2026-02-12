from django.db import models

CATEGORIES = [
   ("voitures", "Voitures"),
   ("motos", "Motos"),
   ("immobilier", "Immobilier"),
   ("commerces", "Commerces"),
   ("emploi", "Emploi"),
   ("multimedia", "Multimédia"),
   ("maison", "Maison"),
   ("jouets", "Jouets"),
   ("mode", "Mode"),
   ("loisirs", "Loisirs"),
   ("services", "Services"),
   ("divers", "Divers"),
]


class Annonce(models.Model):
   titre = models.CharField(max_length=200)
   description = models.TextField(blank=True)

   prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   ville = models.CharField(max_length=120, blank=True)

   category = models.CharField(
       max_length=50,
       choices=CATEGORIES,
       default="divers",
   )

   # --- Coordonnées vendeur ---
   vendeur_nom = models.CharField(max_length=120, blank=True)
   vendeur_email = models.EmailField(blank=True)
   vendeur_telephone = models.CharField(max_length=30, blank=True)

   # --- Localisation / secteur ---
   code_postal = models.CharField(max_length=10, blank=True)
   secteur = models.CharField(max_length=10, blank=True)

   created_at = models.DateTimeField(auto_now_add=True)

   def save(self, *args, **kwargs):
       # Secteur auto = département (2 premiers chiffres du code postal)
       if self.code_postal and len(self.code_postal) >= 2:
           self.secteur = self.code_postal[:2]
       super().save(*args, **kwargs)

   def telephone_masque(self):
       t = (self.vendeur_telephone or "").strip()
       # On garde juste les chiffres pour compter
       digits = "".join(ch for ch in t if ch.isdigit())

       if len(digits) < 4:
           return "****"

       # Affichage simple : 06 ** ** ** 78
       return f"{digits[:2]} ** ** ** {digits[-2:]}"

   def __str__(self):
       return self.titre
