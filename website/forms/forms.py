from django.contrib.auth.models import User
from website.models.models import Profile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('phone_number', 'address', 'city', 'state', 'zipcode')