
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('toppings/', views.toppings, name="toppings"),
    path('pizzas/', views.pizzas, name="pizzas"),
    path('new_topping/', views.createTopping, name="new_topping"),
    path('modify_topping/<str:pk>', views.modifyTopping, name="modify_topping"),
    path('delete_topping/<str:pk>', views.deleteTopping, name="delete_topping"),
    path('new_pizza/', views.createPizza, name="new_pizza"),
    path('modify_pizza/<str:pk>', views.modifyPizza, name="modify_pizza"),
    path('delete_pizza/<str:pk>', views.deletePizza, name="delete_pizza"),
]