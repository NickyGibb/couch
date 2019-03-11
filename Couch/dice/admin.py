# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dice.models import Category, User, Game, Forum

admin.site.register(Category)
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Forum)
