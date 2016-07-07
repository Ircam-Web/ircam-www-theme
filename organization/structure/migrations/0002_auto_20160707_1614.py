# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 14:14
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization structure', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Modelname',
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name'], 'verbose_name': 'person'},
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=mezzanine.core.fields.RichTextField(blank=True, verbose_name='biography'),
        ),
    ]
