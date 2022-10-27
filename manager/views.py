from curses.ascii import HT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from sqlalchemy import null

from .models import *
from .forms import *

# Create your views here.

def home(request):
  return render(request, 'manager/dashboard.html')

def toppings(request):
  toppings = Topping.objects.all()
  context = {'toppings': toppings}
  return render(request, 'manager/toppings.html', context)

def pizzas(request):
  pizzas = Pizza.objects.all()
  context = {'pizzas': pizzas}
  return render(request, 'manager/pizzas.html', context)

def createTopping(request):
  form = ToppingForm()

  if request.method == 'POST':
    form = ToppingForm(request.POST)  
    if form.is_valid():
      form.save()
      return redirect('/toppings')

  context = {'form': form}
  return render(request, 'manager/new_topping.html', context)

def createPizza(request):
  form = PizzaForm()

  if request.method == 'POST':
    form = PizzaForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/pizzas')

  context = {'form': form}
  return render(request, 'manager/new_pizza.html', context)

def modifyPizza(request, pk):
  # handle exceptions thrown when the object does not exist anymore
  try:
    pizza = Pizza.objects.get(id=pk)
  except:
    return redirect('/pizzas')

  form = PizzaForm(instance=pizza)
  if request.method == 'POST':
    form = PizzaForm(request.POST, instance=pizza)  
    if form.is_valid():
      form.save()
      return redirect('/pizzas')

  context = {'form': form}
  # Although this is rendering the new_pizza page, it is filling the form
  # with the data from the selected item and can be modified from there. 
  # NO need to create another template for the same thing.
  return render(request, 'manager/new_pizza.html', context)

def modifyTopping(request, pk):
  # Handle exceptions thrown if the obejct does not exist anymore
  try:
    topping = Topping.objects.get(id=pk)
  except:
    return redirect('/toppings')

  form = ToppingForm(instance=topping)
  if request.method == 'POST':
    form = ToppingForm(request.POST, instance=topping)  
    if form.is_valid():
      form.save()
      return redirect('/toppings')

  context = {'form': form}
  # Although this is rendering the new_topping page, it is filling the form
  # with the data from the selected item and can be modified from there. 
  # NO need to create another template for the same thing.
  return render(request, 'manager/new_topping.html', context)

def deletePizza(request, pk):
  pizza = Pizza.objects.get(id=pk)
  if request.method == 'POST':
    pizza.delete()
    return redirect('/pizzas')
  
  #context = {'pizza': pizza}
  #return render(request, 'manager/pizzas.html', context)

def deleteTopping(request, pk):
  topping = Topping.objects.get(id=pk)
  if request.method == 'POST':
    topping.delete()
    return redirect('/toppings')


