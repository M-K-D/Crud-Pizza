from django.test import SimpleTestCase, TestCase
from manager.forms import *

class TestForms(TestCase):

  def test_pizza_form(self):
    topping1 = Topping.objects.create(name="topping1", quantity=2)
    form = PizzaForm(data={
      'name': 'test_pizza',
      'toppings': [topping1.pk]
    })

    self.assertTrue(form.is_valid())

  def test_topping_form(self):
    validForm = ToppingForm(data={
      'name':'test_topping',
      'quantity':5
    })

    invalidForm = ToppingForm(data={
      'name':'test_topping',
      'quantity':10000000 # Too large
    })

    self.assertTrue(validForm.is_valid())
    self.assertFalse(invalidForm.is_valid())
