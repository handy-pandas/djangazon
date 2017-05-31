from django.shortcuts import render
from website.models.models import Order, Product, ProductOrder

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
    try:
        if request.POST['cancel_payment']:
            order = Order.objects.get(user=request.user, payment=None)
            order.delete()

            context = {}

            template_name = 'order.html'
            return render(request, template_name, context)
    except KeyError:
        pass


    try:
        if 'delete_product' in request.POST:
            product = request.POST['delete_product']
            order = Order.objects.get(user=request.user, payment=None)
            delete_this_product = ProductOrder.objects.filter(order=order, product__id=product)


            print('hello')

            delete_this_product.delete()

    except KeyError:
        pass


    total = 0

    try:
        order = Order.objects.get(user=request.user, payment=None)

    except Order.DoesNotExist:
        
        context = {}

        template_name = 'order.html'
        return render(request, template_name, context)

    for product in order.products.all():
        po = ProductOrder.objects.get(product=product, order=order)
        if product.is_active == 0:
            po.delete()
        if po.quantity > product.quantity:
            po.quantity = product.quantity
            po.save()
        if po.quantity == 0:
            po.delete()
        amount = product.price * po.quantity
        total = total + amount

    context = { 'order': order, 'total': total, 'order_id': order.id }

    template_name = 'order.html'
    return render(request, template_name, context)







