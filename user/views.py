from django.shortcuts import render
from .models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.http import HttpResponseRedirect
# Create your views here.

def sign_in(req):
    return render(req, 'auth.html')

def sign_up(req):
    if req.method == 'POST':
        form = RegistrationForm(data=req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(req, 'sign_up.html', context)
