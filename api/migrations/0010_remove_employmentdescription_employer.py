# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_forgottenpasswordtoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employmentdescription',
            name='employer',
        ),
    ]
