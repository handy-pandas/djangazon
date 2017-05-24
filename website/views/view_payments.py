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

    payments = Payment.objects.filter(user=request.user)

    context = { 'payments': payments, 'order_id': form_data['order_id'] }
    template_name = 'choose_payment.html'
    return render(request, template_name, context)

    