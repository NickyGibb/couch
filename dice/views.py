# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from dice.forms import UserProfileForm, UserForm
from dice.models import User, Game, Category, UserProfile
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django import forms
from dice.forms import RegistrationForm
from django.forms.models import inlineformset_factory



def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'home.html', context=context_dict)

    return response

def events(request):
    HttpResponse("Events page")

    return request

def create_event(request):
    HttpResponse("create event")

    return request



def about(request):

    visitor_cookie_handler(request)
    context_dict = {}
    context_dict['visits'] = request.session['visits']
    response = render(request, 'about.html', context=context_dict)

    return response

def game(request):
    game = Game.objects.all()
    # print(game_list)
    context_dict = {'game': game}
    visitor_cookie_handler(request)

    response = render(request, 'game.html', context_dict)
    return response

def user(request):
    return HttpResponse("This is the user page")
    context_dict = {}

    visitor_cookie_handler(request)

    response = render(request, 'profile.html', context_dict)
    return response

# Creates a new user
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            registered = True
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
                profile.save()
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
                  'register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered
                   })

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check if the user is valid
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenerio would most likely be a HTTP GET.
    else:
        # No contect variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'login.html', {})


def user_logout(request):

     logout(request)
     return HttpResponseRedirect(reverse('home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
             return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form':form})


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

    return render(request, 'category.html', context_dict)

    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def like_game (request):
    game_id = None
    if request.method == 'GET':
        game_id == request.GET['game_id']
    likes = 0
    if game_id:
        game = Game.objects.get(id=ind(game_id))
        if game:
            likes = game.likes +1
            game.likes = likes
            game.save()
    return HttpResponse(likes)

@login_required
def dislike_game (request):
    game_id = None
    if request.method == 'GET':
        game_id = request.GET['game_id']
    dislikes = 0
    if game_id:
        game = Game.objects.get(id=ind(game_id))
        if game:
            likes = game.dislikes +1
            game.dislikes = dislikes
            game.save()
    return HttpResponse(dislikes)


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
    return render(request, 'home', {
        'form': form
    })

@login_required

def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('home')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'picture': userprofile.picture, 'bio': userprofile.bio, 'games_list': userprofile.games_list, 'location': userprofile.player_location })

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.user_name)
        else:
            print(form.errors)

    return render(request, 'dice/profile.html',
              {'userprofile': userprofile, 'selecteduser': user, 'form': form})

def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)
