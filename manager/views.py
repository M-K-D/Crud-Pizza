from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'manager/dashboard.html')

def toppings(request):
  return render(request, 'manager/toppings.html')

def pizzas(request):
  return render(request, 'manager/pizzas.html')