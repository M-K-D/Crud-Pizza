from django.db import models
from pandas import unique
from django.core.validators import MaxValueValidator
from .fields import CaseInsensitiveCharField


class Topping(models.Model):
  name = CaseInsensitiveCharField(max_length=100, null=True, unique=True)
  quantity = models.PositiveIntegerField(null=True, validators=[MaxValueValidator(1000000)])

  def __str__(self):
    return self.name


class Pizza(models.Model):
  name = CaseInsensitiveCharField(max_length=100, null=True, unique=True)
  # on_delete = null will ensure that the pizza still exists after
  toppings = models.ManyToManyField(Topping)

  def __str__(self):
    return self.name
