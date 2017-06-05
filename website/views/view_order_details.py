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
            if str(product.id) == request.POST['product_id']:
                try:
                    product_rating = Rate.objects.get(user=request.user, product=product)
                    product_rating.rate = request.POST['rate']
                except Rate.DoesNotExist:
                    product_rating = Rate(
                        user=request.user,
                        product=product,
                        rate=request.POST['rate']
                        )
                product_rating.save()

        product_dict = { 
            'count': pos_count,
            'title': product.title,
            'price': product.price,
            'description': product.description,
            'id': product.id
            }
        if product.get_rating_for_customer(request.user):
            product_dict['rating'] = product.get_rating_for_customer(request.user)

        product_list.append(product_dict)
        total = total + product.price

    # Render requirements
    template_name = 'order_details.html'
    context = { 'products': product_list, 'total': total, 'order_id': order_id}
    return render(request, template_name, context)
