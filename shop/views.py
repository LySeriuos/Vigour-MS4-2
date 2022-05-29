from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.

# Renamed sort itself to lower_name the original field name would be lost.

# first we check whether sort is in request.get
# If it is. We set it equal to both sort which will be none at this point.
# And sortkey Then we rename sortkey to lower_name
# In the event, the user is sorting by name.
# Then we annotate the current list of products with a new field.
# And check whether the direction is descending
# in order to decide whether to reverse the order.


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
    sort = None
    direction = None
    subcategories = None

    if request.GET:
        # checking if 'sort is in request.GET form
        if 'sort' in request.GET:
            # set qual to both sort. Sort has a value None.
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                # convering name to lowercase
                sortkey = 'lower_name'
                # annotate the current list of products with a new field
                products = products.annotate(lower_name=Lower('name'))
                # sorting by name instead of category's id
            if sortkey == 'category':
                # double underscore syntax allows us to drill into a related model
                sortkey = "category__name"
            # check the direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                # if directioni is descending 
                # so need to use '-' in front of {sort_key}
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            subcategories = Category.objects.filter(subcategory__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'current_subcategories': subcategories
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'You have not permit to manipulate products, login as a Admin!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # capture image if it was submited
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'The product is added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product. Check the form!') 
    else:
        form = ProductForm()
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'You have not permit to manipulate products, login as a Admin!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # get the product information to the form
        form = ProductForm(request.POST, request.FILES, instance=product)
        # checking if changed information is valid
        if form.is_valid():
            # save the product form
            form.save()
            # send the message of success or fail
            messages.success(request, 'The product is updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product. Check the form!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'You have not permit to manipulate products, login as a Admin!')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'The Product is deleted!')
    return redirect(reverse('products'))
