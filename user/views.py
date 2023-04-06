from django.shortcuts import render
from .models import User
from .forms import LoginForm, RegistrationForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.contrib import auth
# Create your views here.

def sign_in(req):
    if req.method == 'POST':
        form = LoginForm(data=req.POST)
        if form.is_valid():
            username = req.POST['username']
            password = req.POST['password']
            user = auth.authenticate(username=username,password=password)
            if user:
                auth.last_login(req. user)
                return HttpResponseRedirect('/')
    else:
        return render(req, 'auth.html')
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
