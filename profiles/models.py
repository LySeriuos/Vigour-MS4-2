from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


# each user can only have one profile.
# And each profile can only be attached to one user
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # all these fields are optional
    user = models.OnetoOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True)
    default_postcode = models.CharField(max_length=20,True=True, blankTrue)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,True=True, blankTrue)
    default_county = models.CharField(max_length=80,True=True, blankTrue)
