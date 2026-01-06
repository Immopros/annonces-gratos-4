from django import forms
from .models import Annonce

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre', 'description', 'prix', 'ville']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }
