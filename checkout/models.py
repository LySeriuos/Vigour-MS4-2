import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


# payment form
class Order(models.Model):
    # editable=False is to create unique order number, generated automatically
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # And updating the delivery cost, order total,
    # and grand total after customer create order insatnce.
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate random and unique order number ysing UUID """
        return uuid.uuid4.hex.upper()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number
        if it hasn't been set already """
        if not_self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)    

# A line-item will be like an individual shopping bag item.
# Relating to a specific order
# Use the information they put into the 
# payment form to create an order instance.
# After it will iterate through the items in the shopping bag.
# Creating an order line item for each one. Then attaching it to the order.
class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(
        max_length=2, null=True, blank=True) # 2kg, 3kg, 4kg, 5kg, 6kg
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
