from django import forms
from .models import Recipe, Categories

class RecipeForm(forms.ModelForm):
    class Meta:
        model =Recipe
        fields = ['title', 'ingredients', 'steps', 'image', 'prep_time', 'category', 'rating']
        widgets = {
    'ingredients': forms.Textarea(attrs={'rows':4, 'placeholder':'List ingredients here'}),
    'steps': forms.Textarea(attrs={'rows':6, 'placeholder':'Describe steps here'}),
    'title': forms.TextInput(attrs={'placeholder':'Recipe Title'}),
    'prep_time': forms.NumberInput(attrs={'placeholder':'Preparation time in minutes'}),
    'rating': forms.NumberInput(attrs={'min':0,'max':5}),
}

