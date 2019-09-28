from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import city_choices, bedrooms_choices, price_choices, bathrooms_choices

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'city_choices' : city_choices,
        'bedrooms_choices' : bedrooms_choices,
        'bathrooms_choices': bathrooms_choices,
        'price_choices' : price_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Get All Realtors
    realtors = Realtor.objects.all().order_by('-hire_date')[:3]
    # Get MVP Realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors' : realtors,
        'mvp_realtors' : mvp_realtors,
    }
    return render(request, 'pages/about.html', context)