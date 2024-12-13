from .models import *
from django import forms 


class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome' : forms.TextInput(attrs={'class' : 'form-control', 'place-holder': 'Nome'}),
            'ordem' : forms.NumberInput(attrs={'class' : 'inteiro form-control', 'placeholder': ''}),
        }

