from django.shortcuts import render
from .models import Advert


def index(request):
    """ A view to return the index page """

    adverts = Advert.objects.all()

    context = {
        'adverts': adverts,
    }
    return render(request, 'home/index.html', context)
