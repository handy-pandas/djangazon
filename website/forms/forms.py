from django.contrib.auth.models import User
from website.models.models import Profile
from website.models.validators.profile_validators import validate_phone, validate_zip
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
    phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(), validators=[validate_phone])
    zipcode = forms.IntegerField(required=False, widget=forms.NumberInput(), validators=[validate_zip])

    class Meta:
        model = Profile
        fields = ('address', 'city', 'state', 'zipcode', 'phone_number')
