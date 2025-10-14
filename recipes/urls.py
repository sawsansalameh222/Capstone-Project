from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('login/', auth_views.LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),# built in django view
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('all_recipes/',views.all_recipes,name='all_recipes'),
]