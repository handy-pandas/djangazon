from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models.models import Profile

def edit_account(request):
    """This function allows the user to change his/her account settings including first name, last name, address, and phone number.
    
    Args:
        request (LIST): A list of tuples from the database pertaining to payment
    
    Returns:
        request: A list of tuples from the database
        template_name (HTML): The webpage's structure
        payment (DICT): This is the profile information stored inside of a dictionary

    Author:
        Nick Nash
    """
    if request.method == "POST":
        form_data = request.POST
        # Grabs user table information
        u = request.user
        u.first_name = form_data['first_name']
        u.last_name = form_data['last_name']
        u.save()
        # Grabs profile table information based on user
        user_profile = Profile.objects.get(pk=u.id)
        user_profile.phone_number = form_data['phone_number']
        user_profile.address = form_data['address']
        user_profile.city = form_data['city']
        user_profile.state = form_data['state']
        user_profile.zipcode = form_data['zipcode']
        user_profile.save()
        context = {'profile': user_profile}
        template_name = 'profile.html'
        return render(request, template_name, context)
    else:
        u = request.user
        user_profile = Profile.objects.get(pk=u.id)
        context = {'profile': user_profile}
        template_name = 'edit_account.html'
        return render(request, template_name, context)
