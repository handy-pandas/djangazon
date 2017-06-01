from django.shortcuts import render
from website.models.models import Order, Product, ProductOrder

def view_order_details(request, order_id):
	"""This function will allow the user to view each individual order's details

	Args:
		request (LIST): A list of tuples from the database pertaining to order
		order_id (INTEGER): The primary key of the chosen order

	Returns:
		request: A list of tuples from the database
		template_name (HTML): The webpage's structure
		payment (DICT): The orders completed by the current user, products on the order, and the order total

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
