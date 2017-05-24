from django.shortcuts import render
from website.models.models import Order, Product, Payment

def confirm_order(request):
    """This function updates the payment type in the order table.
    
    Arguments:
        request (List): django magic for request
    
    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        context (Dict): This is an empty dictionary

    Author:
        Talbot Lawrence
        Adam Myers
    """
    # order_id is form_data['order_id']
    # payment_id is form_date['payment_id']
    form_data = request.POST
    order = Order.objects.get(id=form_data['order_id'], payment=None)
    order.payment = form_data['payment_id']
    order.save()

    print(form_data)


    template_name = 'confirmation.html'
    return render(request, template_name, {})