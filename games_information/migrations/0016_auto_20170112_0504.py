# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0015_auto_20170110_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]