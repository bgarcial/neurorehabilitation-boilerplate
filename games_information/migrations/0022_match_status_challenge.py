# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_information', '0021_auto_20161030_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='status_challenge',
            field=models.CharField(choices=[('Aceptado', 'Aceptado'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], default=True, max_length=40, verbose_name='Estado del desafío'),
        ),
    ]
