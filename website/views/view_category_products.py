from django.shortcuts import render
from website.models.models import Product
from website.models.models import Category

def category_products(request):

    categories = Category.objects.all()

    context = { 'categories': categories }

    template_name = 'categories/category_product_list.html'
    return render(request, template_name, context)