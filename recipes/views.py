from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    recipes =Recipe.objects.all()
    return render(request,'recipes/home.html',{'recipes':recipes})

def about(request):
    return render(request,'recipes/about.html')

def profile(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request,'recipes/profile.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    if request.method=='POST':
        form=RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)  
            recipe.user = request.user       
            recipe.save()                    
            return redirect('home')
    else:
        form=RecipeForm()
    return render(request,'recipes/add_recipe.html',{'form':form})

@login_required
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)  
    if request.method == 'POST':
        recipe.delete()
        return redirect('profile')

@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk, user=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form})


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

def all_recipes(request):
    recipes =Recipe.objects.all()
    return render(request,'recipes/all_recipes.html',{'recipes':recipes})
