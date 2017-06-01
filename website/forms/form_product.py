from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from website.models.models import Product

class ProductForm(forms.ModelForm):



	local_delivery = forms.BooleanField(required= False)
	city = forms.CharField(required = False)

	class Meta:
		model = Product
		fields = ('title', 'description', 'price', 'quantity','image_path', 'category', 'local_delivery','city')

