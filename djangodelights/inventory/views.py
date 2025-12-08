from django.shortcuts import render
from .models import Ingredient, RecipeRequirements, MenuItem, Purchase
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
# Create your views here.

class IngredientListView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"

class PurchaseListView(ListView):
    model = Purchase
    template_name = "purchase_list.html"

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = "inventory/ingredients_confirm_delete.html"
    success_url = reverse_lazy('ingredientslist')