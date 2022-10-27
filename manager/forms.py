from django.forms import ModelForm
from django import forms
from .models import Topping, Pizza

# Form that is served when creating a new topping
# Must have meta class for the model to be properly assigned, see Django docs for info
class ToppingForm(ModelForm):
  class Meta:
    model = Topping
    fields = '__all__'

class PizzaForm(ModelForm):
  class Meta:
    model = Pizza
    fields = ('name','toppings',)


  toppings = forms.ModelMultipleChoiceField(
        queryset= Topping.objects.all(),
        widget=forms.CheckboxSelectMultiple)