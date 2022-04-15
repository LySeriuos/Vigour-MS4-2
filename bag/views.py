from django.shortcuts import render, redirect

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
    # check if session exist and if doesn't create one with {}
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    # print(request.session['bag'])
    # use this to see if the quantity is added to the session cockies
    return redirect(redirect_url)