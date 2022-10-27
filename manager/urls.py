from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('toppings/', views.toppings),
    path('pizzas/', views.pizzas),
    path('new_topping/', views.createTopping),
    path('new_pizza/', views.createPizza),
]