# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 21:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games_information', '0007_match_fichaje_players_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='away_team_players_acept',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team_players_acept',
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_players_accept',
            field=models.ManyToManyField(blank=True, related_name='away_team_players_accept', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_players_accept',
            field=models.ManyToManyField(blank=True, related_name='home_team_players_accept', to=settings.AUTH_USER_MODEL),
        ),
    ]
