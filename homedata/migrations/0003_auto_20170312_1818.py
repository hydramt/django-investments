# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homedata', '0002_auto_20170312_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exchanges',
            old_name='ccreated',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='exchanges',
            old_name='eenabled',
            new_name='enabled',
        ),
        migrations.RenameField(
            model_name='exchanges',
            old_name='eexch',
            new_name='exch',
        ),
        migrations.RenameField(
            model_name='exchanges',
            old_name='eexch_full',
            new_name='exch_full',
        ),
        migrations.RenameField(
            model_name='exchanges',
            old_name='mmodified',
            new_name='modified',
        ),
    ]