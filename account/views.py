from .forms import LoginForm
from .forms import RegistrationForm
from .forms import UserProfileForm

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def login(request):
    if request.method == "GET":
        login_form = LoginForm()
        context = dict(
            login_form=login_form,
        )
        return render(request, 'account/login.html', context)

    elif request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            data = login_form.cleaned_data
            user = authenticate(username=data['username'],
                                password=data['password'])

            if user:
                target_url = reverse('blog:index')
                return redirect(target_url)
            else:
                return HttpResponse("User name is not correct")
        else:
            return HttpResponse("Input your name and pwd!")


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = new_user
            user_profile.save()

            return HttpResponse("Create a user successfully.")

        else:
            return HttpResponse("sorry, You can not register")


    else:
        user_form = RegistrationForm()
        user_profile_form = UserProfileForm()

        context = dict(
            form=user_form,
            user_profile_form=user_profile_form,
        )
        return render(request, 'account/register.html', context=context)
