from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.forms.forms import UserForm
from website.forms.form_product import ProductForm
from website.models.model_product import Product


def product_details(request):
	"""This function allows the product's information to be displayed as prescribed.

	Author:
	    Nick Nash
	
	Args:
	    request (TYPE): A list of tuples from the database
	
	Returns:
	    request: A list of tuples from the database
	    template_name (HTML): The webpage's structure
	    product (Dict): This is the product's information stored inside of a dictionary
	"""
	product = Product.objects.all() 
	template_name = 'product/product_details.html'
	return render(request, template_name, {'product': product})
