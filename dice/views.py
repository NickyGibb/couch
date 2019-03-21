# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from dice.forms import UserProfileForm, UserForm
from dice.models import User, Game, Category, UserProfile
from datetime import datetime
from django.contrib.auth.decorators import login_required
from registration.backends.simple.views import RegistrationView
from django import forms
from django.core.urlresolvers import reverse



def home(request):
    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    response = render(request, 'dice/home.html', context=context_dict)

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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'dice/register.html', {'user_form': user_form, 'profile_form':profile_form, 'registered':registered})

def user_login(request):
    error = None

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

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

    else:
        return render(request, 'dice/login.html', {})


def user_logout(request):

     logout(request)
     return HttpResponseRedirect(reverse('home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')


        user = authenticate(username=username, password=password)



        if user:

            if user.is_active:

                login(request, user)
                return HttpResponseRedirect(reverse('dice:home'))

            else:
                return HttpResponse("Your Couch CO-OP account is disabled.")

        else:
            print("Invalid login details: {0}, {1})".format(username, password))
            return HttpResponse("Invalid login details provided.")

    else:
        return render(request, 'dice/login.html',{})


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
         else:
             print(form.errors)

     context_dict = {'form':form}

     return render(request, 'dice/profile_registration.html', context_dict)

class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')



@login_required
def profile(request, user_name):
    try:
        user = User.objects.get(user_name=user_name)
    except User.DoesNotExist:
        return redirect('home')
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'website': userprofile.website,'picture': userprofile.picture})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.user_name)
        else:
            print(form.errors)

    return render(request, 'dice/profile.html',
              {'userprofile': userprofile, 'selecteduser': user, 'form': form})
