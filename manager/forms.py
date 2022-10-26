from django.forms import ModelForm

from .models import Topping

# Form that is served when creating a new topping
# Must have meta class for the model to be properly assigned, see Django docs for info
class ToppingForm(ModelForm):
  class Meta:
    model = Topping
    fields = '__all__'
