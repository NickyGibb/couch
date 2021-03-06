# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dice.models import  *




class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('game_name',)}
    list_display = ('game_name', 'game_type', 'game_genre', 'game_image')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'picture', 'bio', 'player_endorsements', 'player_location', 'games_list')



admin.site.register(Category, CategoryAdmin)

admin.site.register(Game, GameAdmin)
admin.site.register(UserProfile)
