from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from website.models.models import Profile

def edit_account(request):
    """Summary
    
    Args:
        request (TYPE): Description
    
    Returns:
        TYPE: Description

    Author:
        Nick Nash
    """
    if request.method == "POST":
        form_data = request.POST

        # context = { 'payments': payment }
        # u = User.objects.get(id=user.request.id)
        u = request.user
        u.first_name = form_data['first_name']
        u.last_name = form_data['last_name']
        u.save()

        user_profile = Profile.objects.get(pk=u.id)
        user_profile.phone_number = form_data['phone_number']
        user_profile.address = form_data['address']
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
