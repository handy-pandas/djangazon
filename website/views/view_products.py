from django.shortcuts import render
from website.models.models import Product

def list_category_products(request, category_id):
    # chosen_product = Product.objects.get(pk=product_id)
    all_products_in_cat = Product.objects.all(pk=category_id)
    template_name = 'categoryproducts.html'
    return render(request, template_name, {'products': all_products_in_cat})