from django.shortcuts import render
from website.models.models import Order, Product, ProductOrder

def view_order_details(request, order_id):
	"""This function will allow the user to view each individual order's details

	Args:
		request (TYPE): Description

	Author:
		Nick Nash
	"""

	# Grabbing all necessary information
	o = Order.objects.get(id=order_id)
	p = o.products.all()

	# Getting order total
	total = 0
	for product in p:
		total = total + product.price

	# Render requirements
	template_name = 'order_details.html'
	context = {'order': o, 'products': p, 'total': total}
	return render(request, template_name, context)
