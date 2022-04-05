from django.shortcuts import render
from .models import Product

# Create your views here.


def shop(request):
    """A view to return the shop page"""
    products = Product.objects.all()

    context = {
        'shop': products,
    }

    return render(request, 'shop/shop.html', context)

# copied from home/views.py.

  
