from django.db import models

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

