# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from dice.models import  User,Game,Forum, Category




def home(request):
    return HttpResponse("This is the home page")
def about(request):
    return HttpResponse("This is the about page")
def game(request):
    game_list = Game.objects.order_by('-name')[:10]
    context_dict = {'Games': game_list}
    return render(request, 'dice/game.html', context_dict)

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
