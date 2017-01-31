# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0019_auto_20170129_2304'),
        ('userprofiles', '0004_auto_20170129_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='team',
        ),
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='games_information.Team', verbose_name='Equipo en el que juega'),
            preserve_default=False,
        ),
    ]
