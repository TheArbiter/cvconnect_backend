# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20161019_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='compensation',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]