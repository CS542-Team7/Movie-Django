# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 00:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20170425_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularity',
            name='movieid',
            field=models.OneToOneField(default=' ', on_delete=django.db.models.deletion.CASCADE, to='movie.Movie'),
        ),
    ]
