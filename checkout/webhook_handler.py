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
        intent = stripe.PaymentIntent.modify(event)
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a handle_payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
