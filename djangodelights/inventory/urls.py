from django.urls import path
from . import views

urlpatterns = [
    path("ingredients/list/", views.IngredientListView.as_view(), name="ingredientslist"),
    path("purchase/list/", views.PurchaseListView.as_view(), name="purchaselist"),
    path("ingredients/delete/<pk>", views.IngredientDeleteView.as_view(), name="deleteingredient")
]