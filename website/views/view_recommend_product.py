from django.shortcuts import render, redirect
from website.forms.form_recomend import RecommendationForm
from website.models.models import Recommendation, Product
from django.contrib.auth.models import *
from django.core.exceptions import ObjectDoesNotExist




def recommend_product(request, product_id):
	"""
	this method does stuff for recommending products
	"""

	if request.method == 'POST':
		chosen_product = Product.objects.get(pk=product_id)
		try:
			form_data = request.POST
			recommend_form = RecommendationForm()
			friend = form_data['receiver']
			the_receiver = User.objects.get(username=friend)

			r = Recommendation(
			product = chosen_product,
			receiver = the_receiver
			)
			r.save()
			template_name = 'product/product_details.html'
			return render(request, template_name, {'product': chosen_product})
		except User.DoesNotExist:
			template_name = 'recommend_product.html'
			return render(request, template_name, {'product': chosen_product})

	elif request.method == 'GET':
		chosen_product = Product.objects.get(pk=product_id)
		template_name = 'recommend_product.html'
		return render(request, template_name, {'product': chosen_product})