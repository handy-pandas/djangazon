from django.shortcuts import render
from website.forms.form_payment import PaymentForm
from website.models.models import Payment

def add_payment(request):
	if request.method == 'GET':
		template_name = 'addpayment.html'
		payment_form = PaymentForm()
		return render(request, template_name, {'payment_form': payment_form})

	elif request.method == 'POST':
		form_data = request.POST
		payment_form = PaymentForm()
		template_name = 'addpayment.html'
		return render(request, template_name, {'payment_form': payment_form})
		
		p = Payment(
			name = form_data['name'],
			account_number = form_data['account_number'],
			user = request.user
		)

		p.save()
		template_name = 'profile.html'
		return render(request, template_name, {})