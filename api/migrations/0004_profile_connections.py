# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_company_companymanager_educationdescription_employmentdescription_skill_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='connections',
            field=models.ManyToManyField(to='api.Profile'),
        ),
    ]
