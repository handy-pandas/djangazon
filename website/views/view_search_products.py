import operator
from django.shortcuts import render
from django.db.models import Q
from django.template import RequestContext
from website.models.models import Product



def search_products(request):
    """This function allows user to search for items by their title or description or city for local delivery 

    
    Arguments:
        request (GET): retrieves data from the search input and filters through products
        
    Returns:     
        return (render): The search products results are rendered on the search products page
    
    Author:
        Angela Lee
    """
    form_data = request.GET
    iterable_form_data = form_data.dict()
    print("\niterable_form_data: {}\n".format(iterable_form_data))
    
    search_box = iterable_form_data['Search']

    try:
        if iterable_form_data['local_delivery']:
            products = Product.objects.filter(Q(city__icontains=search_box))

    except KeyError:
        products = Product.objects.filter(Q(description__icontains=search_box) | Q(title__icontains=search_box))

    template_name = 'search_products.html'

    return render(request, template_name, {'products': products})