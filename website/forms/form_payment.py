from django.contrib.auth.models import User
from django import forms
from website.models.models import Payment

class PaymentForm(forms.ModelForm):

    class Meta:
        model = Payment
        widgets = {
                    'name': forms.TextInput(attrs={'class': 'form-control'}),
                    'account_number': forms.NumberInput(attrs={'class': 'form-control'})
                }
        fields = ('name', 'account_number')