from django.shortcuts import render
from ecommerceapp.models import Product
from django.db.models import Q

# Create your views here.

def searchResult(request):
    product = None
    query = None
    
    if 'q' in request.GET:
        query = request.GET.get('q')
        product = Product.objects.all().filter(Q(name_contains=query) | Q(description_contains=query))
    return render(request, 'serach.html', {'query':query, 'product':product})
