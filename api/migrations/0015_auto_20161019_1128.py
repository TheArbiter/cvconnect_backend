# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20161019_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='position',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='compensation',
            field=models.TextField(blank=True, default=''),
        ),
    ]
