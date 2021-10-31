from django import forms

from django.forms import widgets

from .models import recipe

class Recipeform(forms.ModelForm):
    class Meta:
        model = recipe
        fields = "__all__"
        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the name of your Recipe'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description of your recipes and steps on how to prepare it'}),
            'timetaken':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the time taken (in minutes) to prepare your recipe'}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':'The image of your recipe'})
        }