# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('object_maps', '0007_auto_20170315_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objects',
            name='Time1',
        ),
    ]
