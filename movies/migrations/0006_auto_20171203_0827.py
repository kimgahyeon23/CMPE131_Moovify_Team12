# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_movieinfo_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='cast',
            field=models.CharField(default='No cast', max_length=2000),
        ),
    ]
