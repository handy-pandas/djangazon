from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models.models import Profile, User
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
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()

        profile = Profile.objects.get(pk=request.user.id)
        profile_form = ProfileForm(request.POST or None, instance=profile)

        if profile_form.is_valid():
            profile_form.save()
        else:
            return show_edit_account(request, error=profile_form.errors.values())

        context = {'profile': profile, 'user': user}
        template_name = 'profile.html'
        return render(request, template_name, context)
    else:
        return show_edit_account(request)

def show_edit_account(request, error=False):
    u = request.user
    user_form = EditUserForm(initial={'first_name': u.first_name, 'last_name': u.last_name})

    u_p = Profile.objects.get(pk=u.id)
    profile_form = ProfileForm(initial={'address': u_p.address, 'phone_number': u_p.phone_number, 'city': u_p.city, 'state': u_p.state, 'zipcode': u_p.zipcode})

    if error == False:
        context = {'profile_form': profile_form, 'user_form': user_form}
    else:
        context = {'profile_form': profile_form, 'user_form': user_form, 'message': error}
        

    template_name = 'edit_account.html'
    return render(request, template_name, context)



