# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-03 02:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('movie_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('query', models.CharField(default='', max_length=100)),
                ('poster', models.CharField(default='No poster available', max_length=100)),
                ('summary', models.CharField(default='No summary at this time', max_length=200)),
                ('bigposter', models.CharField(default='No poster available', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=10)),
                ('comment', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
