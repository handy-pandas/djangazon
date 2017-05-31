from django.shortcuts import render
from website.forms.form_payment import PaymentForm
from website.models.models import Payment

def add_payment(request):
	"""This function allows user to add payment data for their profile to database.

	
	Arguments:
	    request (POST): Sends data from payment form to payment table 
	    
	Returns:     
		return (render): The profile form with add payment link is displayed
	
	Author:
	    Angela Lee

	"""

	if request.method == 'GET':
		template_name = 'addpayment.html'
		payment_form = PaymentForm()
		return render(request, template_name, {'payment_form': payment_form})

	elif request.method == 'POST':
		form_data = request.POST
		payment_form = PaymentForm()
		
		p = Payment(
			name = form_data['name'],
			account_number = form_data['account_number'],
			user = request.user
		)

		p.save()
		template_name = 'view_payment_types.html'
		return render(request, template_name, {'payment_form': payment_form})