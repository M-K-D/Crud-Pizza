from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

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

  context = {'form': form}

  return render(request, 'manager/new_topping.html', context)

def createPizza(request):
  form = PizzaForm()

  if request.method == 'POST':
    form = PizzaForm(request.POST)
    print(form)
    if form.is_valid():
      form.save()

  context = {'form': form}

  return render(request, 'manager/new_pizza.html', context)



