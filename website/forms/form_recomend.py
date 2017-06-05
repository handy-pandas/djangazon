from django.contrib.auth.models import User
from django import forms
from website.models.models import RecommendProduct

class RecommendationForm(forms.ModelForm):
	
	class Meta:
			model = RecommendProduct
			fields = ('receiver', 'product')