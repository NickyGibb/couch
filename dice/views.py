# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from dice.models import  User,Game,Forum




def home(request):
    return HttpResponse("This is the home page")
def about(request):
    return HttpResponse("This is the about page")
def game(request):
    return render(request, 'dice/game.html')

def user(request):
    return HttpResponse("This is the user page")
def forum(request):
    return HttpResponse("This is the Forum page")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'hyfy/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def register_profile(request):
    form = UserProfileForm()
if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES)
    if form.is_valid(): user_profile = form.save(commit=False)
    user_profile.user = request.user
    user_profile.save()
return redirect('index')
else:
print(form.errors)

context_dict = {'form':form}

return render(request, 'dice/profile_registration.html', context_dict)

@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
        except User.DoesNotExist:
        return redirect('home')

userprofile = UserProfile.objects.get_or_create(user=user)[0]
form = UserProfileForm(
    {'website': userprofile.website, 'picture': userprofile.picture})

if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profile', user.username)
        else: print(form.errors)
return render(request, 'rango/profile.html',
              {'userprofile': userprofile, 'selecteduser': user, 'form': form})
