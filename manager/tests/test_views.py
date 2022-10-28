from django.test import TestCase, Client
from django.urls import reverse, resolve
from manager.models import *

class TestViews(TestCase):

  def test_pizzas_page(self):
    client = Client()
    response  = client.get(reverse('pizzas'))

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'manager/pizzas.html')

  def test_toppings_page(self):
    client = Client()
    response  = client.get(reverse('toppings'))

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'manager/toppings.html')



