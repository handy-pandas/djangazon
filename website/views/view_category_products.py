from django.shortcuts import render
from website.models.models import Product
from website.models.models import Category

def category_products(request):

    categories = Category.objects.all()

    context = { 'products': products, 'categories': categories, 'list_of_counts': list_of_counts }

    template_name = 'categories/category_product_list.html'
    return render(request, template_name, context)