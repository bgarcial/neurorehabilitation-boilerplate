# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-29 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0014_auto_20161029_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('GOALKEEPER', 'Portero - PT'), ('DEFENDER', 'Defensa Central - DFC'), ('RIGHT_DEFENDER', 'Defensa Lateral Derecho - LD'), ('LEFT_DEFENDER', 'Defensa Lateral Izquierdo- LI'), ('MIDFIELDER_FORWARD', 'Media Punta (por el centro adelantado) - MP'), ('MIDFIELDER_CENTER', 'Medio Centro (en el centro) - MC'), ('MIDFIELDER_DEFENSIVE', 'Medio Campo Defensivo - MCD'), ('MIDFIELDER_LEFT', 'Medio Izquierda - MI'), ('MIDFIELDER_RIGHT', 'Medio Derecha - MD'), ('FORWARD_CENTER', 'Delantero Centro (siempre pendientes de meter goles) - DC'), ('FORWARD_RIGHT', 'Extremo Derecho (los más adelantados por la banda) - ED'), ('FORWARD_LEFT', 'Extremo Izquierdo  - EI'), ('SECOND_FORWARD', 'Segundo Delantero - SD')], max_length=554, verbose_name='Posicion'),
        ),
    ]
