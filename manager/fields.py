# fields.py
from django.db.models import CharField
from django_case_insensitive_field import CaseInsensitiveFieldMixin

# This is necessary for the char model fields to be case insensitive, so that 
# we can easily detect attempts to add duplicate items in the database. 
# ie. topping name: Sausage == sausage

class CaseInsensitiveCharField(CaseInsensitiveFieldMixin, CharField):
    """[summary]
    Makes django CharField case insensitive \n
    Extends both the `CaseInsensitiveMixin` and  CharField \n
    Then you can import 
    """

    def __init__(self, *args, **kwargs):

        super(CaseInsensitiveFieldMixin, self).__init__(*args, **kwargs) 