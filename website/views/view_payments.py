from django.shortcuts import render
from website.models.models import Order, Product, Payment

def view_payments(request):
    """This function allows the user after the confirmation of an order to choose a payment type.
    
    Arguments:
        request (List): A list of tuples from the database pertaining to payment
    
    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        payment (Dict): This is the payment information stored inside of a dictionary

    Author:
        Talbot Lawrence
        Adam Myers
    """
    form_data = request.POST


    try:
        if form_data['order_id']:
            payments = Payment.objects.filter(user=request.user, is_active=1)
            context = { 'payments': payments, 'order_id': form_data['order_id'] }
            template_name = 'choose_payment.html'
            return render(request, template_name, context)
    except KeyError:
        pass

    try:
        if form_data['delete_payment']:
            payment_id = form_data['delete_payment']

            payment = Payment.objects.get(user=request.user, id=payment_id)
            order_on_payment = Order.objects.filter(user=request.user, payment=payment)

            if not order_on_payment:
                payment.delete()
            else:
                # 1 is True, 0 is False
                payment.is_active = 0
                payment.save()

            
    except KeyError:
        pass

    payments = Payment.objects.filter(user=request.user, is_active=1)
    context = { 'payments': payments }
    template_name = 'view_payment_types.html'
    return render(request, template_name, context)



    