from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_bag(request):
    """ A view to return the shoping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add quantity of the specified product to the shoping bag """
    # need to convert it to an integer
    # since it'll come from the template as a string.

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
            else:
                # just set it equal to the quantity.
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            # if item has no siz using this logic:
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    # use this to see if the quantity is added to the session cockies
    return redirect(redirect_url)


def update_bag(request, item_id):
    """ Update quantity of the specified product to the specified amount """
    # need to convert it to an integer
    # since it'll come from the template as a string.
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
        else:
            # just set it equal to the quantity.
            del bag[item_id]['items_by_size'][size]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop[item_id]
            # remove the item
            # entirely by using the pop function
    request.session['bag'] = bag
    # print(request.session['bag'])
    # use this to see if the quantity is added to the session cockies
    return redirect(reverse('view_bag'))
