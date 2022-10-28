from django.test import SimpleTestCase
from django.urls import reverse, resolve
from manager.views import *

class TestUrls(SimpleTestCase):

  def test_home(self):
    url = reverse('home')
    self.assertEquals(resolve(url).func, home)

  def test_toppings(self):
    url = reverse('toppings')
    self.assertEquals(resolve(url).func, toppings)
    
  def test_pizzas(self):
    url = reverse('pizzas')
    self.assertEquals(resolve(url).func, pizzas)

  def test_new_topping(self):
    url = reverse('new_topping')
    self.assertEquals(resolve(url).func, createTopping)
 
  def test_modify_topping(self):
    url = reverse('modify_topping', args=['id'])
    self.assertEquals(resolve(url).func, modifyTopping)

  def test_new_pizza(self):
    url = reverse('new_pizza')
    self.assertEquals(resolve(url).func, createPizza)

  def test_modify_pizza(self):
    url = reverse('modify_pizza', args=['id'])
    self.assertEquals(resolve(url).func, modifyPizza)

  def test_delete_pizza(self):
    url = reverse('delete_pizza', args=['id'])
    self.assertEquals(resolve(url).func, deletePizza)

  def test_delete_topping(self):
    url = reverse('delete_topping', args=['id'])
    self.assertEquals(resolve(url).func, deleteTopping)

 