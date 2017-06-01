from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models.models import Profile
from website.forms.forms import ProfileForm, EditUserForm, UserForm

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
        Adam Myers
    """
    if request.method == "POST":

        form_data = request.POST

        user = request.user
        user_form = UserForm(request.POST or None, instance=user)
        if user_form.is_valid():
            user_form.save()

        profile = Profile.objects.get(pk=user.id)
        profile_form = ProfileForm(request.POST or None, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

        context = {'profile': profile}
        template_name = 'profile.html'
        return render(request, template_name, context)
    else:
        u = request.user
        user_form = EditUserForm(initial={'first_name': u.first_name, 'last_name': u.last_name})

        u_p = Profile.objects.get(pk=u.id)
        profile_form = ProfileForm(initial={'address': u_p.address, 'phone_number': u_p.phone_number, 'city': u_p.city, 'state': u_p.state, 'zipcode': u_p.zipcode})

        context = {'profile_form': profile_form, 'user_form': user_form}

        template_name = 'edit_account.html'
        return render(request, template_name, context)



