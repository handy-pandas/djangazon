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

    orders = Order.objects.filter(user__id=1, payment=None)
    for o in orders:
        for product in o.products.all():
            total = total + product.price

    print(total)
    context = { 'orders': orders, 'total': total }

    template_name = 'order.html'
    return render(request, template_name, context)