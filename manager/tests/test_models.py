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
    pizza = Pizza.objects.create(name="test")
    topping1 = Topping.objects.create(name="topping1")
    topping2 = Topping.objects.create(name="topping2")
    pizza.toppings.set([topping1.pk, topping2.pk])

    self.assertEqual(pizza.toppings.count(), 2)
    self.assertEqual(pizza.name, 'test')