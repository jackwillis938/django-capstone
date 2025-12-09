from django.db import models
from django.db.models import Sum
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    measurement_unit = models.CharField(max_length=50)
    available_quantity = models.FloatField()
    price_per_unit = models.FloatField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
    def get_ingredient_cost(self):
        item_cost = 0
        #Get all recipe reqs for the menu item purchased
        requirements = RecipeRequirements.objects.filter(menu_item = self)
        
        for req in requirements:
            item_cost += req.ingredient.price_per_unit*req.quantity
        return item_cost
    
class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True, blank=False)
    date_purchased = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.menu_item:
            return self.menu_item.name
        else:
            return "Purchased Item (Deleted)"

#------------------------------------------------------------------------------------------
# Model-related logic:

def calculate_revenue():
    revenue = Purchase.objects.aggregate(total=Sum('menu_item__price'))
    return revenue['total'] or 0

def calculate_total_cost():
    total_cost = 0
    for purchase in Purchase.objects.all():
        total_cost += purchase.menu_item.get_ingredient_cost()
    return total_cost

def calculate_profit():
    return calculate_revenue() - calculate_total_cost()

def auto_update_inventory(item: Purchase):
    requirements = item.menu_item.reciperequirements_set.all()

    for req in requirements:
        ingredient = req.ingredient
        ingredient.available_quantity -= req.quantity
        ingredient.save()
