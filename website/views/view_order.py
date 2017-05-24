from django.shortcuts import render
from website.models.models import Order, Product

def view_order(request):
    """This function allows the order's information to be displayed as prescribed.
    
    Arguments:
        request (List): A list of tuples from the database pertaining to order
    
    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        order (Dict): This is the order information stored inside of a dictionary

    Author:
        Talbot Lawrence
        Adam Myers
    """
    # request.user.id
    # order = Order.objects.filter(user=request.user, payment=None)
    total = 0

    try:
        order = Order.objects.get(user=request.user, payment=None)

    except Order.DoesNotExist:
        order = Order(
            user = request.user,
            payment = None
            )
        order.save()

    for product in order.products.all():
        total = total + product.price

    context = { 'order': order, 'total': total, 'order_id': order.id }

    template_name = 'order.html'
    return render(request, template_name, context)

