# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 10:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dice', '0003_auto_20190312_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forum',
            name='post_user',
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
    ]
