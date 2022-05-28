from django.http import HttpResponse
from django.conf import settings

from .models import Order, OrderLineItem
from shop.models import Product
from profiles.models import UserProfile

import json
import time

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
        # metadata contains username and other info
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Shipping data details cleaning
        for field, value in shipping_details.Address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:                
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.address1
                profile.default_street_address2 = shipping_details.address.address2
                profile.default_county = shipping_details.address.state
                profile.save()

        # Check if order exists in database
        # get the order data
        order_exists = False
        # here setting up loop times before it do some action
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    user_profile=profile,
                    email_name__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.address1,
                    street_address2__iexact=shipping_details.address.address2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            # check if order doesn't exists in database
            except Order.DoesNotExist:
                # before creating a new order time.sleep gives 1 second to loop
                # and try to find order 5 times in 1 second before it will create a new order
                attempt += 1
                time.sleep(1)
                # if order exists iåt will give a success message
        if order_exists:            
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: '
                        'Verified order already in database',
                status=200)
                # and if it doesn't exists it will create new one
        else:                    
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        email_name=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.state,
                        original_bag=bag,
                        stripe_pid=pid,
                )
                # get the Product ID out of the bag
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    # if its value is an integer it means the item that doesn't have sizes.
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                        # if the item has sizes. It will iterate through each size 
                        # and creates a line item accordingly.
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
                         
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS:' 
                    'Created order in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a handle_payment_intent_payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
