from django.shortcuts import render
from website.models.models import Product
from website.models.models import Category

def category_products(request):
    """This function allows the product's information to be displayed as prescribed.

    Arguments:
        request (List): A list of tuples from the database pertaining to categories

    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        categories (Dict): This is the categories information stored inside of a dictionary

    Author:
        Adam Myers
    """
    categories = Category.objects.all()

    context = { 'categories': categories }

    template_name = 'categories/category_product_list.html'
    return render(request, template_name, context)
