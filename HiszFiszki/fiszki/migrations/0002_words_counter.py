# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiszki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='counter',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
