# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Game(models.Model):
    game_name = models.CharField(max_length=128, unique=True)
    game_type = models.CharField(max_length=128, unique=False)
    game_genre = models.CharField(max_length=128, unique=False)
    player_number = models.IntegerField(default=0)
    game_views = models.IntegerField(default=0)
    likes =  models.IntegerField(default=0)
    dislikes =  models.IntegerField(default=0)
    game_image = models.ImageField(upload_to='game_image', blank=True)
    game_site = models.URLField(max_length=250, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.game_name)
        super(Game, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'games'

    def __str__(self):
        return self.game_name


class Event(models.Model):
    event_name = models.CharField(max_length=200)

    event_start = models.DateTimeField(null=True)
    event_end = models.DateTimeField(null=True)
    event_location = models.CharField(max_length=200, null=True)
    game = models.CharField(max_length=200)
    description = models.TextField(default='Please add a description:')

    def __str__(self):
        return self.event_name


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    user_image = models.ImageField(upload_to='user_image', blank=True)
    bio = models.TextField(default='', blank=True)
    player_location = models.CharField(max_length=200, default='', blank=True)
    games_list = models.CharField(max_length=200, null=True)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
