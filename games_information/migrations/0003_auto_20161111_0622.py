# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0002_auto_20161111_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='name',
            field=models.CharField(db_index=True, max_length=150, primary_key=True, serialize=False, unique=True),
        ),
    ]