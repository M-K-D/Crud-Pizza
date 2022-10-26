from django.db import models
from pandas import unique
#from django.db.models import UniqueConstraint
#from django.db.models.functions import Lower
from .fields import CaseInsensitiveCharField


class Topping(models.Model):
  topping_name = CaseInsensitiveCharField(max_length=100, null=True, unique=True)
  quantity = models.PositiveIntegerField(null=True)

class Pizza(models.Model):
  pizza_name = CaseInsensitiveCharField(max_length=100, null=True)
  # on_delete = null will ensure that the pizza still exists after
  toppings = models.ManyToManyField(Topping)