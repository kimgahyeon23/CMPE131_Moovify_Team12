# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-30 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20171130_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='movie',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='summary',
            field=models.CharField(default='No summary at this time', max_length=200),
        ),
        migrations.DeleteModel(
            name='page',
        ),
    ]