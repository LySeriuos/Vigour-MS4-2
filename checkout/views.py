from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    # to get the total all I need to do is get 
    # the grand_total key out of the current bag
    current_bag = bag_contents(reuquest)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KqEATK3tyBr1GDCbUxKLbErhD4WUPQGgGVNuiGLHKrkUQqu2BCvjCh6APrPoItCPozL4tzuEsvmzbVFch6oE5Rx00lXqnggoQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
