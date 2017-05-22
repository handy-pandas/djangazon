from django.contrib.auth.models import User
from django import forms
from website.models.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'category')
