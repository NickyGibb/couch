# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class User(models.Model):

    user_name = models.CharField(max_length=128, unique=False)
    user_email = models.CharField(max_length=128, unique=True)
    #score = models.FloatField(_(u"Score"), choices= SCORE_CHOICES, default=3.0)


    def __str__(self):
        return self.user_name

class Game(models.Model):

    game_name = models.CharField(max_length=128, unique =True)
    game_type = models.CharField(max_length=128, unique= False)
    game_genre = models.CharField(max_length=128, unique=False)
    #score = models.FloatField(_(u"Score"), choices= SCORE_CHOICES, default=3.0)
    player_number = models.IntegerField(max_length= 3,unique = True)
    game_image = models.ImageField(upload_to= 'game_image', blank=True)

    def __str__(self):
        return self.game_name

class Forum(models.Model):

    post_title = models.CharField(max_length=128, unique = False)
    post_user = models.ForeignKey(User)



    def __str__(self):
        return self.post_title

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    attendees = models.ManyToManyField(User, related_name='attendees')
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    location = models.CharField(max_length=200, null=True)
    game = models.CharField(max_length=200)
    description = models.TextField(default='Please add a description')

    def __str__(self):
        return self.event_name


