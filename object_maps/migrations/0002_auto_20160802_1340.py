# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('object_maps', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='object',
            new_name='objects',
        ),
    ]
