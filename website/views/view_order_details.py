from django.shortcuts import render
from website.models.models import Order, Product, ProductOrder, Rate

def view_order_details(request, order_id):
    """This function will allow the user to view each individual order's details

    Args:
        request (LIST): A list of tuples from the database pertaining to order
        order_id (INTEGER): The primary key of the chosen order

    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        payment (DICT): The orders completed by the current user, products on the order, and the order total

    Author:
        Nick Nash
        Adam Myers
    """
    # Grabbing all necessary information
    order = Order.objects.get(id=order_id)

    # Getting order total
    total = 0
    product_list = list()

    for product in order.products.all().distinct():
        pos = ProductOrder.objects.filter(product=product, order=order)
        pos_count = pos.count()

        if request.method == 'POST':
            if product.id == request.POST['product_id']:
                product_rating = Rate.objects.get_or_create(user=request.user, product=product)
                product_rating.rating = request.POST['rate']
                product_rating.save()

        product_dict = dict()
        product_dict['count'] = pos_count
        product_dict['title'] = product.title
        product_dict['price'] = product.price
        product_dict['description'] = product.description
        product_dict['id'] = product.id
        product_list.append(product_dict)
        total = total + product.price

    # Render requirements
    template_name = 'order_details.html'
    context = { 'products': product_list, 'total': total, 'order_id': order_id}
    return render(request, template_name, context)
