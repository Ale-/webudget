# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_auto_20170913_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='YearData',
            new_name='Dataset',
        ),
    ]
