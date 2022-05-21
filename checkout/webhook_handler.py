from django.http import HttpResponse
from django.conf import settings

from .models import Order, OrderLineItem
from shop.models import Product
from profiles.models import UserProfile


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    # function for getting atributes from stripe
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a handle_payment_intent_succeeded webhook from stripe
        """
        intent = event.data.object(event)
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Shipping data details cleaning
        for field, value in shipping_details.Address.items():
            if value == "":
                shipping_details.address[field] = None
        # Check if order doesn't exists in database
        # get the order data
        order_exists = False
        order = Order.objects.get(
            full_name__iexact=shipping_details.name,
            email_name__iexact=shipping_details.email,
            phone_number__iexact=shipping_details.phone,
            country__iexact=shipping_details.country,
            postcode__iexact=shipping_details.postal_code,
            town_or_city__iexact=shipping_details.city,
            street_address1__iexact=shipping_details.address1,
            street_address2__iexact=shipping_details.address2,
            grand_total=grand_total,
        )
        order_exists = True        
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success: Verified order already in database',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a handle_payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
