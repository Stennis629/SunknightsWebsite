# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-22 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0011_auto_20161222_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicpointsubmission',
            name='points',
            field=models.SmallIntegerField(default=0),
        ),
    ]
