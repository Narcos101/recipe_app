from django import forms

from .models import recipe

class Recipeform(forms.ModelForm):
    class Meta:
        model = recipe
        fields = '__all__'