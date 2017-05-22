from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext

from website.forms.forms import UserForm
from website.forms.form_product import ProductForm
from website.models.model_product import Product


def product_details(request):
	# Line 13 will be changed, need to find out how to pull current information
	product = Product.objects.all() 
	template_name = 'product/product_details.html'
	return render(request, template_name, {'product': product})