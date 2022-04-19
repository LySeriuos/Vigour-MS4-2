from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KqEATK3tyBr1GDCbUxKLbErhD4WUPQGgGVNuiGLHKrkUQqu2BCvjCh6APrPoItCPozL4tzuEsvmzbVFch6oE5Rx00lXqnggoQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
    