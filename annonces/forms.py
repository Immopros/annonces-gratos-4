from django import forms
from .models import Annonce


class AnnonceForm(forms.ModelForm):
   class Meta:
       model = Annonce
       fields = [
           'titre',
           'description',
           'prix',
           'ville',
           'code_postal',
           'secteur',
           'category',
           'vendeur_nom',
           'vendeur_email',
           'vendeur_telephone',
       ]

       widgets = {
           'description': forms.Textarea(attrs={'rows': 6}),
       }
