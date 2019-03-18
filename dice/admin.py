# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dice.models import User, Game, Category
from dice.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('game_name',)}
    list_display = ('game_name', 'game_type', 'game_genre', 'game_image')


class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user_name',)}
    list_display = ('user_name','user_email', 'user_views', 'user_endorsements', 'user_image')




admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
