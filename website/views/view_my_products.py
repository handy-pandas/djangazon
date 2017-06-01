from django.shortcuts import render
from website.models.models import Product, Order, ProductOrder

def my_products(request):
    """
    Display all of the products for a given category.

    Arguments:
        request (GET): Get data from Product table

    Returns:
        render, Combines template_name with the given dictionary and passes HttpResponse object with that rendered text.

    Author:
        Adam Myers
    """
    if request.method == 'GET':

        product_for_sale = Product.objects.filter(seller=request.user, is_active=1, quantity__gt=0)
        template_name = 'my_products.html'
        context = {'products': product_for_sale}
        return render(request, template_name, context)

    elif request.method == 'POST':

        data = request.POST

        product = Product.objects.get(id=data['product_id'])

        pos = ProductOrder.objects.select_related("order", "product").filter(product=product, order__payment__isnull=False).count()

        if pos == 0:
            product.delete()
        else:
            product.is_active = 0
            product.save()


        product_for_sale = Product.objects.filter(seller=request.user, is_active=1, quantity__gt=0)
        template_name = 'my_products.html'
        context = {'products': product_for_sale}
        return render(request, template_name, context)


