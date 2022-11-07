
from django.urls import path
from . import views

urlpatterns = [
    # Giving the pattern a name value allows you to refer to the url from a template(html)
    # and in the views. Also, if the url path ever changes, you can use reverse( <url_name> ) to always get
    # the correct path based on the name rather than the changing every reference to the url path iteself. 
    # This follows DRY(DONT REPEAT YOURSELF). ie. Redirect(reverse('new_topping')) NOT Redirect(reverse('/new_topping'))
    # Note: I forgot to implement this methodology in my views, TODO.
    path('', views.home, name="home"),
    path('toppings/', views.toppings, name="toppings"),
    path('pizzas/', views.pizzas, name="pizzas"),
    path('new_topping/', views.createTopping, name="new_topping"),
    path('modify_topping/<str:pk>', views.modifyTopping, name="modify_topping"),
    path('delete_topping/<str:pk>', views.deleteTopping, name="delete_topping"),
    path('new_pizza/', views.createPizza, name="new_pizza"),
    path('modify_pizza/<str:pk>', views.modifyPizza, name="modify_pizza"),
    path('delete_pizza/<str:pk>', views.deletePizza, name="delete_pizza"),
]
