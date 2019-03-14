# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from dice.models import  User,Game, Category




def home(request):

    category_list = Category.objects.order_by('-name')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'dice/home.html', context_dict)


def about(request):

    return render(request, 'dice/about.html')

def game(request):
    game_list = Game.objects.order_by('-views')[:10]
    context_dict = {'Games': game_list}
    return render(request, 'dice/game.html', context_dict)

def user(request):
    return HttpResponse("This is the user page")

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
     return HttpResponseRedirect(reverse('index'))


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
