from django.shortcuts import render
from .models import Advert
from products.models import Product

def index(request):
    """ A view to return the index page """

    adverts = Advert.objects.all()
    products = Product.objects.all()

    context = {
        'adverts': adverts,
        'products': products,
    }
    return render(request, 'home/index.html', context)


