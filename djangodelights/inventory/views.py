from django.shortcuts import render
from .models import Ingredient, RecipeRequirements, MenuItem, Purchase, calculate_total_cost, calculate_profit, calculate_revenue
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementsForm
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

class MenuItemListView(ListView):
    model = MenuItem
    template_name = "inventory/menu_item_list.html"

def financial_dashboard(request):
    rev = calculate_revenue()
    cost = calculate_total_cost()
    profit = calculate_profit()
    
    context = {'revenue': rev, 'cost': cost, 'profit': profit}

    return render(request, 'inventory/financial_dashboard.html', context)

class IngredientCreateView(CreateView):
    form_class = IngredientForm
    template_name = "inventory/ingredient_create.html"
    success_url = reverse_lazy('ingredientslist')

class MenuItemCreateView(CreateView):
    form_class = MenuItemForm
    template_name = "inventory/menu_item_create.html"
    success_url = reverse_lazy('ingredientslist')

class PurchaseCreateView(CreateView):
    form_class = PurchaseForm
    template_name = "inventory/purchase_create.html"
    success_url = reverse_lazy('ingredientslist')

class RecipeRequirementsCreateView(CreateView):
    form_class = RecipeRequirementsForm
    template_name = "inventory/recipe_requirements_create.html"
    success_url = reverse_lazy('ingredientslist')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = "inventory/ingredient_update.html"
    success_url = reverse_lazy('ingredientslist')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = "inventory/menu_item_update.html"
    success_url = reverse_lazy('menu')
