# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='director',
            field=models.CharField(default='No director', max_length=200),
        ),
    ]
