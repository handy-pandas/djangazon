from django.shortcuts import render
from website.models.models import Product

def list_products(request):
    all_products = Product.objects.all()
    print('xxxxxx',len(all_products))
    return render(request, template_name, {'products': all_products})


