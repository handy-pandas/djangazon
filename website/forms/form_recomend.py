from django.contrib.auth.models import User
from django import forms
from website.models.models import Recommendation

class RecommendationForm(forms.ModelForm):

	class Meta:
			model = Recommendation
			fields = ('receiver', 'product')