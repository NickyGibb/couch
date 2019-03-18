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
from dice.models import  User,Game, Category
from datetime import datetime
from django.contrib.auth.decorators import login_required



def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'dice/home.html', context=context_dict)

    return response


def about(request):

    visitor_cookie_handler(request)
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    response = render(request, 'dice/about.html', context=context_dict)

    return response

def game(request):
    game = Game.objects.all()
    # print(game_list)
    context_dict = {'game': game}
    visitor_cookie_handler(request)

    response = render(request, 'dice/game.html', context_dict)
    return response

def user(request):
    return HttpResponse("This is the user page")
    context_dict = {}

    visitor_cookie_handler(request)

    response = render(request, 'dice/profile.html', context_dict)
    return response

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


def user_logout(request):

     logout(request)
     return HttpResponseRedirect(reverse('home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
     visits = int(get_server_side_cookie(request,'visits','1'))
     last_visit_cookie = get_server_side_cookie(request,
     'last_visit',
     str(datetime.now()))
     last_visit_time = datetime.strptime(last_visit_cookie[:-7],
      '%Y-%m-%d %H:%M:%S')
     if (datetime.now() - last_visit_time).days > 0:
         visits = visits + 1
         request.session['last_visit'] = str(datetime.now())
     else:
         request.session['last_visit'] = last_visit_cookie

     request.session['visits'] = visits

def show_category(request, category_name_slug):

    context_dict= {}

    try:

        category = Category.objects.get(slug = game_name_slug)

        games = Game.objects.filter(category = category)

        context_dict['games'] = games

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['games'] = None

    return render(request, 'dice/category.html', context_dict)

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
    if form.is_valid():
        user_profile = form.save(commit=False)
        user_profile.user = request.user
        user_profile.save()

return redirect('home')

else: print(form.errors)

context_dict = {'form':form}

return render(request, 'profile_registration.html', context_dict)

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')

@login_required
def profile(request, username):
    try: user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')
userprofile = UserProfile.objects.get_or_create(user=user)[0]
form = UserProfileForm(
    {'website': userprofile.website,
     'picture': userprofile.picture})

if request.method == 'POST':
    form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profile', user.username)
        else: print(form.errors)
return render(request, 'dice/profile.html',
              {'userprofile': userprofile, 'selecteduser': user, 'form': form})



