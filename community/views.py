from django.shortcuts import render

# Create your views here.


def trainers(request):
    """ A view to return the index page """
    return render(request, 'community/our_trainers.html')
