from django.shortcuts import render
from website.models.models import Order, Product

def view_payments(request):
    """This function allows the after the confirmation of an order to choose a payment type.
    
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

    payments = Payment.objects.filter(user__id=1)

    context = { 'payments': payments }

    template_name = 'choose_payment.html'
    return render(request, template_name, context)