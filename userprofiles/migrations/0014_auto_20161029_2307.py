# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-29 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0013_auto_20161026_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('Portero', 'Portero'), ('Defensa Central', 'Defensa Central'), ('Defensa lateral derecho', 'Defensa lateral derecho'), ('Defensa lateral izquierdo', 'Defensa lateral izquierdo'), ('Segundo delantero', 'Segundo delantero')], max_length=554, verbose_name='Posicion'),
        ),
    ]
