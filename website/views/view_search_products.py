import operator
from django.shortcuts import render
from django.db.models import Q
from django.template import RequestContext
from website.models.models import Product



def search_products(request):
    '''
    blablblba something about searching
    '''

    # terms = request.GET.get('terms')
    # if request.method == 'GET':
    if request.GET.get('q', False):    
        form_data = request.GET
        print("form_data", form_data)
        iterable_form_data = form_data.dict()
        print("form_data", iterable_form_data)
        for (k,v) in iterable_form_data.items():
            print(k)
            print(v)

        search_box = iterable_form_data[k]
        # search_box = form_data["search_box"]
        print("search box", search_box)
        
        products = Product.objects.all()

        # q = Q(description__icontains=search_box) | Q(title__icontains=search_box)
        # for term in term_list[1:]:
        #     q.add((Q(description__icontains=term) | Q(title__icontains=term)), q.connector)

        products = Product.objects.filter(Q(description__icontains=search_box) | Q(title__icontains=search_box))
        template_name = 'search_products.html'

        return render(request, template_name, {'products': products})


