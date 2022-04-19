from django import forms
from .models import Order


# Meta options telling django which model it'll be associated with
# and which fields to render.
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)


def __init__(self, *args, **kwargs):
    """ Add placeholders and classes, remove auto-generated
    labels and set autofocus on first field """
    # First call the default init method to set the form up as it would be by default
    super().__init__(*args, **kwargs)
    # dictionary of placeholders which will show up
    # in the form fields
    placeholders = {
         'full_name': 'Full Name',
         'email': 'Email Address',
         'phone_number': 'Phone Number',
         'country': 'Country',
         'postcode': 'Postal Code',
         'town_or_city': 'Town or City',
         'street_address1': 'Street Address 1',
         'street_address2': 'Street Address 2',
         'county': 'County',
        }
