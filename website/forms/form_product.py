from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from website.models.models import Product

class ProductForm(forms.ModelForm):

	local_delivery = forms.BooleanField(required= False)
	city = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Product
		widgets = {
		            'title': forms.TextInput(attrs={'class': 'form-control'}),
		            'description': forms.TextInput(attrs={'class': 'form-control'}),
		            'price': forms.NumberInput(attrs={'class': 'form-control'}),
		            'quantity': forms.NumberInput(attrs={'class': 'form-control'})

		}
		fields = ('title', 'description', 'price', 'quantity','image_path', 'category', 'local_delivery','city')