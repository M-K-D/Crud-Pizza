from django.test import TestCase
from manager.models import *
from manager.views import toppings

class TestModels(TestCase):

  def setUp(self):
    self.topping= Topping.objects.create(name='test', quantity=10)

  def test_topping(self):
    self.assertEquals(self.topping.name, 'test')
    self.assertEquals(self.topping.quantity, 10)

  def test_pizza(self):
    self.pizza = Pizza.objects.create(name='test')
    self.assertEquals(self.pizza.name, 'test')