# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-17 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginbar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='mapping',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
