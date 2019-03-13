# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dice.models import User, Game, Category

class GameAdmin(admin.ModelAdmin):
    list_display = ('game_name', 'game_type', 'game_genre', 'game_image')
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email', 'user_views', 'user_endorsements', 'user_image')
class ForumAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'post_type', 'post_user')

admin.site.register(Category)
admin.site.register(User, UserAdmin)
admin.site.register(Game, GameAdmin)
