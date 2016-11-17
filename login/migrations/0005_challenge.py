# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 01:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_lesson_expected_output'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_name', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('expected_output', models.CharField(default=None, max_length=200)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Lesson')),
            ],
        ),
    ]
