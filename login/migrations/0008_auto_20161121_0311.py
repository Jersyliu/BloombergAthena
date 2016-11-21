# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 03:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20161118_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='point_value',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='challengeprogress',
            name='notes',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='lesson',
            name='point_value',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='newuser',
            name='picture',
            field=models.CharField(default='homepage/images/profilepic.png', max_length=200),
        ),
        migrations.AddField(
            model_name='newuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='progress',
            name='notes',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='challengeprogress',
            name='progress_until_now',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='summary',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='progress',
            name='progress_until_now',
            field=models.TextField(default=None),
        ),
    ]