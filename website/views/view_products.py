from django.shortcuts import render
from website.models.models import Product

def list_category_products(request, category_id):
    """
    Display all of the products for a given category.

    Arguments:
        request (GET): Get data from Product table,
        category_id(foreign key): The Id of the selected category.

    Returns: render, Combines template_name with the given dictionary and passes HttpResponse object with that rendered text.

    Author:
        wocaldwell
    """
    all_products_in_cat = Product.objects.filter(category_id=category_id, is_active=1)
    category_name = all_products_in_cat[0].category
    print(category_name)
    template_name = 'categoryproducts.html'
    return render(request, template_name, {'products': all_products_in_cat, 'name': category_name})