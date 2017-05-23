from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.forms.forms import UserForm
from website.forms.form_product import ProductForm
from website.models.models import Product, Category


def product_details(request, product_id):
	"""This function allows the product's information to be displayed as prescribed.

	Author:
	    Nick Nash
	
	Args:
	    request (List): A list of tuples from the database
	
	Returns:
	    request: A list of tuples from the database
	    template_name (HTML): The webpage's structure
	    product (Dict): This is the product's information stored inside of a dictionary
	"""
	chosen_product = Product.objects.get(pk=product_id)
	template_name = 'product/product_details.html'
	return render(request, template_name, {'product': chosen_product})

# def chosen_product_category(request):
# 	chosen_category 
# category = Category.objects.get(pk=form_data['category']),
