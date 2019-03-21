# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-21 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200)),
                ('event_start', models.DateTimeField(null=True)),
                ('event_end', models.DateTimeField(null=True)),
                ('event_location', models.CharField(max_length=200, null=True)),
                ('game', models.CharField(max_length=200)),
                ('description', models.TextField(default='Please add a description:')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=128, unique=True)),
                ('game_type', models.CharField(max_length=128)),
                ('game_genre', models.CharField(max_length=128)),
                ('player_number', models.IntegerField(default=0)),
                ('game_views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('game_image', models.ImageField(blank=True, upload_to='game_image')),
                ('game_site', models.URLField(blank=True, max_length=250)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'games',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, upload_to='user_image')),
                ('bio', models.CharField(max_length=800)),
                ('player_location', models.CharField(max_length=200, null=True)),
                ('games_list', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
