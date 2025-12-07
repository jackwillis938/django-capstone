from django.shortcuts import render
from .models import Ingredient, RecipeRequirements, MenuItem, Purchase
from django.views.generic import ListView
# Create your views here.

class InventoryListView(ListView):
    model = Ingredient
    
