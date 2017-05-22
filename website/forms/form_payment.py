from django.contrib.auth.models import User
from django import forms
from website.models.models import Payment

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        fields = ('name', 'account_number')
