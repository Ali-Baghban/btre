from django.shortcuts import render , get_object_or_404
from .choices import city_choices,price_choices, bedrooms_choices, bathrooms_choices
from .models import Listing

def index(request):
    listings = Listing.objects.all()
    count = Listing.objects.all().count()
    context = { 'listings' : listings , 'count' : count}
    return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    count = Listing.objects.all().count()
    queryset_list = Listing.objects.order_by('-list_date')
    # City filter
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            count = queryset_list.count()
    # Price filter
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            count = queryset_list.count()
    # bedrooms filter
    if 'bedroom' in request.GET:
        bedroom = request.GET['bedroom']
        if bedroom:
            queryset_list = queryset_list.filter(bedrooms__lte=bedroom)
            count = queryset_list.count()
    # Bathrooms filter
    if 'bathroom' in request.GET:
        bathroom = request.GET['bathroom']
        if bathroom:
            queryset_list = queryset_list.filter(bathrooms__lte=bathroom)
            count = queryset_list.count()

    context = {
        'city_choices' : city_choices,
        'bedrooms_choices' : bedrooms_choices,
        'price_choices' : price_choices,
        'bathrooms_choices' : bathrooms_choices,
        'listings' : queryset_list,
        'values' : request.GET,
        'count': count,
    }
    return render(request, 'listings/search.html', context)