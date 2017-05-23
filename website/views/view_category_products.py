from django.shortcuts import render
from website.models.models import Product


def list_category_products(request):
    all_products_in_cat = Product.objects.all()
    template_name = 'categoryproducts.html'
    return render(request, template_name, {'products': all_products_in_cat})
