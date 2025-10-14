from django.shortcuts import render
from .models import Recipe
# Create your views here.
def home(request):
    recipes =Recipe.objects.all()
    return render(request,'recipes/home.html',{'recipes':recipes})

def about(request):
    return render(request,'recipes/about.html')

def profile(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request,'recipes/profile.html', {'recipes': recipes})

def add_recipe(request):
    return render(request,'recipes/add_recipe.html')

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def all_recipes(request):
    recipes =Recipe.objects.all()
    return render(request,'recipes/all_recipes.html',{'recipes':recipes})
