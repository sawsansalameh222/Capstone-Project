from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categories(models.Model):
    # id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    # id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    ingredients=models.TextField(null=True, blank=True)
    steps=models.TextField(null=True, blank=True)
    image=models.ImageField(upload_to='recipes/', null=True, blank=True)
    prep_time=models.IntegerField(help_text="Preparation time in minutes", null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(null=True,blank=True,default=0,help_text="Rate recipe out of 5")

    def __str__(self):
        return self.title

