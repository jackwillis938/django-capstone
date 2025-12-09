from django.urls import path, include
from . import views

urlpatterns = [
    path("ingredients/list/", views.IngredientListView.as_view(), name="ingredientslist"),
    path("purchase/list/", views.PurchaseListView.as_view(), name="purchaselist"),
    path("ingredients/delete/<pk>", views.IngredientDeleteView.as_view(), name="deleteingredient"),
    path("menu/", views.MenuItemListView.as_view(), name="menu"),
    path("financial-dashboard/", views.financial_dashboard, name="financialdashboard"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredientscreate"),
    path("menu/create/", views.MenuItemCreateView.as_view(), name="menuitemcreate"),
    path("purchase/create/", views.PurchaseCreateView.as_view(), name="purchasecreate"),
    path("recipe-requirements/create/", views.RecipeRequirementsCreateView.as_view(), name="reciperequirementscreate"),
    path("ingredients/update/<pk>", views.IngredientUpdateView.as_view(), name="ingredientsupdate"),
    path("menu/update/<pk>", views.MenuItemUpdateView.as_view(), name="menuitemupdate"),
    path("recipe-requirements/update/<pk>", views.RecipeRequirementsUpdateView.as_view(), name="reciperequirementsupdate"),
    path("accounts/", include('django.contrib.auth.urls')),
    path('signup/', views.signup_view, name='signup')
]