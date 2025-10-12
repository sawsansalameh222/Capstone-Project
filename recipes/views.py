from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/home.html')

def about(request):
    return render(request,'recipes/about.html')

def profile(request):
    return render(request,'recipes/profile.html')

def add_recipe(request):
    return render(request,'recipes/add_recipe.html')