from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def shop(request):
    """A view to return the shop page"""
    """check if GET is requested and if 'q' is in that request
    I'll set a variable equal to a Q object. Where the name contains the query.
    Or the description contains the query.
    The pipe here is what generates the or statement.
    And the i in front of contains makes the queries case insensitive."""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) 
            products = products.filter(queries)


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
