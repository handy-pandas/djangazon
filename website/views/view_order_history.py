from django.shortcuts import render
from website.models.models import Order, Product, ProductOrder

def view_order_history(request):
	"""This function allows the user to see his/her order history

	Args:
		request (TYPE): Description

	Returns:
		request: A list of tuples from the database
		template_name (HTML): The webpage's structure
		payment (DICT): The orders completed by the current user

	Author:
		Nick Nash
	"""

	template_name = 'order_history.html'
	all_orders = Order.objects.filter(user=request.user, payment__isnull=False)
	context = {'orders': all_orders}
	return render(request, template_name, context)
