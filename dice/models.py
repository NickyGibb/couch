# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class User(models.Model):

    user_name = models.CharField(max_length=128, unique=False)
    user_email = models.CharField(max_length=128, unique=True)
    user_views = models.IntegerField(default=0)
    user_endorsements = models.IntegerField(default=0)
    user_image = models.ImageField(upload_to= 'user_image', blank=True)



    def __str__(self):
        return self.user_name

class Game(models.Model):

    game_name = models.CharField(max_length=128, unique =True)
    game_type = models.CharField(max_length=128, unique= False)
    game_genre = models.CharField(max_length=128, unique=False)
    player_number = models.IntegerField(default=0)
    game_views = models.IntegerField(default=0)
    game_endorsements = models.IntegerField(default=0)
    game_image = models.ImageField(upload_to= 'game_image', blank=True)

    def __str__(self):
        return self.game_name

class Forum(models.Model):

    post_title = models.CharField(max_length=128,default="", unique = False)
    post_user = models.ForeignKey(User)
    post_type = models.CharField(max_length=128,default="", unique= False)
    post_views = models.IntegerField(default=0)
    post_endorsements = models.IntegerField(default=0)



    def __str__(self):
        return self.post_title
