from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the shoping bag page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add quantity of the specified product to the shoping bag """
    """ need to convert it to an integer since it'll come from the template as a string. """

    quantity = int(request.POST.get('quantity'))