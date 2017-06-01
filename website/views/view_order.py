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

    new_list = list()

    for product in order.products.all().distinct():
        pos = ProductOrder.objects.filter(product=product, order=order)
        pos_count = pos.count()

        if product.is_active == 0:
            pos.delete()
        if product.quantity == 0:
            pos.delete()
        if pos_count > product.quantity:
            diff = pos_count - product.quantity
            pos.delete()
            create_productorders(product.quantity, product, order)
            pos = ProductOrder.objects.filter(product=product, order=order)
            pos_count = pos.count()


        new_dict = dict()
        new_dict['count'] = pos_count
        new_dict['title'] = product.title
        new_dict['price'] = product.price
        new_dict['id'] = product.id
        new_list.append(new_dict)

        amount = product.price * pos_count
        total = total + amount



    context = { 'order': order, 'total': total, 'order_id': order.id, 'product_list': new_list }

    template_name = 'order.html'
    return render(request, template_name, context)

def create_productorders(quantity, product_in, order_in):
    for each in range(quantity):
        po = ProductOrder(
            product=product_in,
            order=order_in
            )
        po.save()







