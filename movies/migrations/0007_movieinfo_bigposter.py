# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-30 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20171130_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='bigposter',
            field=models.CharField(default='No poster available', max_length=100),
        ),
    ]