# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0010_auto_20160707_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='sub_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='sub title'),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_title_fr',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='sub title'),
        ),
    ]
