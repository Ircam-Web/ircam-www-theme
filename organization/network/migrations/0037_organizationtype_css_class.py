# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0036_auto_20161005_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationtype',
            name='css_class',
            field=models.CharField(blank=True, help_text='Determine color on map.', max_length=64, null=True, verbose_name='class css'),
        ),
    ]
