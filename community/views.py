from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Trainers

# Create your views here.


def community(request):
    """ A view to return the index page """

    trainer = Trainers.objects.all()
    context = {
        "trainer": trainer,
        }

    return render(request, 'community/our_trainers.html', context)
