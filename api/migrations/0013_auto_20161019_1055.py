# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-19 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20161016_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='company',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='compensation',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='jobposting',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
