from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.forms.forms import UserForm
from website.forms.form_product import ProductForm
from website.models.models import Product, Category, Order, ProductOrder


def product_details(request, product_id):
	"""This function allows the product's information to be displayed as prescribed.

	Author:
	    Nick Nash
	    wocaldwell

	Args:
	    request (List): A list of tuples from the database

	Returns:
	    request: A list of tuples from the database
	    template_name (HTML): The webpage's structure
	    product (Dict): This is the product's information stored inside of a dictionary
	"""

	if request.method == "POST":

		chosen_product = Product.objects.get(pk=product_id)
		template_name = 'product/product_details.html'

		try:
			order = Order.objects.get(user=request.user, payment=None)

		except Order.DoesNotExist:
			order = Order(
				user = request.user,
				payment = None
				)
			order.save()	

		try:
			po = ProductOrder.objects.get(order=order, product=chosen_product)
			po.quantity = po.quantity + 1
			po.save()

		except ProductOrder.DoesNotExist:
			po = ProductOrder(
				order = order,
				product = chosen_product,
				quantity = 1
				)
			po.save()


		return render(request, template_name, {'product': chosen_product})


	elif request.method == 'GET':
		chosen_product = Product.objects.get(pk=product_id)
		template_name = 'product/product_details.html'
		return render(request, template_name, {'product': chosen_product})
