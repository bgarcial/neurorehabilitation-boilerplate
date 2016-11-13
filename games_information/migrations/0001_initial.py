# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('field_type', models.CharField(choices=[('Grama natural', 'Grama natural'), ('Grama sintetica', 'Grama sintetica')], default=False, max_length=20, verbose_name='Tipo de material/grama de la cancha')),
                ('modality', models.CharField(max_length=40, verbose_name='Modalidad')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='fields')),
                ('location', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_match_away_team', models.BooleanField(default=False)),
                ('match_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status_challenge', models.CharField(choices=[('Aceptado', 'Aceptado'), ('Pendiente', 'Pendiente'), ('Cancelado', 'Cancelado')], default=True, max_length=40, verbose_name='Estado del desafío')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(blank=True, db_index=True, max_length=64, primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='fields', verbose_name='Imagen de la plantilla o escudo')),
                ('modality', models.CharField(choices=[('Fútbol 11', 'Fútbol 11'), ('Fútbol 8', 'Fútbol 8'), ('Fútbol 7', 'Fútbol 7'), ('Fútbol 6', 'Fútbol 6'), ('Fútbol 5', 'Fútbol 5')], default=True, max_length=40, verbose_name='Modalidad')),
                ('game_day', models.CharField(max_length=150, verbose_name='Reservas o frecuencia de juego')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCompetitionCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('location', models.CharField(max_length=150)),
                ('fields', models.ManyToManyField(to='games_information.Field')),
            ],
        ),
    ]
