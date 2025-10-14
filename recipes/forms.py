from django import forms
from .models import Recipe, Categories

class RecipeForm(forms.ModelForm):
    class Meta:
        model =Recipe
        fields = ['title', 'ingredients', 'steps', 'image', 'prep_time', 'category', 'rating']
