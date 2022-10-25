from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, 'manager/dashboard.html')

def toppings(request):
  return HttpResponse('Manage Toppings')

def pizzas(request):
  return HttpResponse('Manage pizza recipes')