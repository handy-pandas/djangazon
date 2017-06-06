from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.forms.forms import UserForm
from website.forms.form_product import ProductForm
from website.models.models import Product, Category, Order, ProductOrder, Opinion, Recommendation


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
	template_name = 'product/product_details.html'
	chosen_product = Product.objects.get(pk=product_id)

	if 'like' in request.POST:
		liked_product = chosen_product
		opinion = Opinion(
			like=1,
			product=liked_product,
			user=request.user
		)

		opinion.save()

	if 'dislike' in request.POST:
		disliked_product = chosen_product
		opinion = Opinion(
			like=0,
			product=disliked_product,
			user=request.user
		)

		opinion.save()

	if 'product.id' in request.POST:



		try:
			order = Order.objects.get(user=request.user, payment=None)

		except Order.DoesNotExist:
			order = Order(
				user = request.user,
				payment = None
				)
			order.save()

		try:
			pos = ProductOrder.objects.filter(order=order, product=chosen_product).count()
			if chosen_product.quantity > pos:
				po = ProductOrder(
				order = order,
				product = chosen_product
				)
				po.save()

		except ProductOrder.DoesNotExist:
			po = ProductOrder(
				order = order,
				product = chosen_product
				)
			po.save()




	elif request.method == 'GET':
		chosen_product = Product.objects.get(pk=product_id)
		template_name = 'product/product_details.html'
	return render(request, template_name, {'product': chosen_product})
