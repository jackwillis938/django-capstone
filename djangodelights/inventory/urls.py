from django.urls import path
from . import views

urlpatterns = [
    path("ingredients-list/", views.InventoryListView.as_view(), name="ingredientslist"),
]