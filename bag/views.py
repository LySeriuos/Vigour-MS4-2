from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from shop.models import Product

# Create your views here.

def view_bag(request):
    """ A view to return the shoping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of the specified product to the shoping bag """
    # need to convert it to an integer
    # since it'll come from the template as a string.
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # if product size is in request.post it will be set equal to that.
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # check if session exist and if doesn't create one with {}
    bag = request.session.get('bag', {})

    # If the items not already in the bag we just need to add it.
    # do it as a dictionary with a key of 'items_by_size'.
    if size:
        if item_id in list(bag.keys()):
            # Need to check if another item of the same id
            # and same size already exists.
            if size in bag[item_id]['items_by_size'].keys():
                # if so increment the quantity for that size and otherwise
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                # just set it equal to the quantity.
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
            # if item has no size using this logic:
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    # print(request.session['bag'])
    # use this to see if the quantity is added to the session cockies
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update quantity of the specified product to the specified amount """
    # need to convert it to an integer
    # since it'll come from the template as a string.
    # in case if product not found
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    # if product size is in request.post it will be set equal to that.
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # check if session exist and if doesn't create one with {}
    bag = request.session.get('bag', {})

    # If the items not already in the bag we just need to add it.
    # do it as a dictionary with a key of 'items_by_size'.
    if size:
        if quantity > 0:
            # if quantity is greater than zero set the items quantity
            # accordingly or just remove the item.
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            # just set it equal to the quantity.
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} quantity from your bag')
            # remove the item
            # entirely by using the pop function
    request.session['bag'] = bag
    # print(request.session['bag'])
    # use this to see if the quantity is added to the session cockies
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} quantity from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)