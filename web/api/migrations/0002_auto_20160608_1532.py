# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='father_id',
            field=models.CharField(blank=True, default=None, max_length=32, verbose_name='\u7236\u4efb\u52a1ID'),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='group_id',
            field=models.CharField(blank=True, default=None, max_length=32, verbose_name='\u4efb\u52a1\u7ec4ID'),
        ),
    ]
