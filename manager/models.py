from pyexpat import model
from django.db import models


class Topping(models.Model):
  name = models.CharField(max_length=100, null=True)
  quantity = models.PositiveIntegerField(null=True)

class Pizza(models.Model):
  name = models.CharField(max_length=100, null=True)
  # on_delete = null will ensure that the pizza still exists after
  toppings = models.ManyToManyField(Topping)