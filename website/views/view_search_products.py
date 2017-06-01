import operator
from django.shortcuts import render
from django.db.models import Q
from django.template import RequestContext
from website.models.models import Product



def search_products(request):
    """This function allows user to search for items by their title or description

    
    Arguments:
        request (GET): retrieves data from the search input and filters through products
        
    Returns:     
        return (render): The search products results are rendered on the search products page
    
    Author:
        Angela Lee

    """

    # if request.GET.get('q', False):    
    form_data = request.GET
    print("\nform_data: {}\n".format(form_data))
    iterable_form_data = form_data.dict()
    print("\niterable_form_data: {}\n".format(iterable_form_data))
    
    for (k,v) in iterable_form_data.items():
        search_box = iterable_form_data[k]
        print("\nsearch_box: {}\n".format(search_box))
    products = Product.objects.all()
    print("\nproducts: {}\n".format(products))

    if value == "local_checked":
        products = Product.objects.filter(Q(city__icontains=search_box))
    else:
        products = Product.objects.filter(Q(description__icontains=search_box) | Q(title__icontains=search_box))
    template_name = 'search_products.html'

    return render(request, template_name, {'products': products})