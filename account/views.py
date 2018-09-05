from .forms import LoginForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    login_form = LoginForm()
    context = dict(
        login_form=login_form,
    )
    return render(request, 'account/login.html', context)
