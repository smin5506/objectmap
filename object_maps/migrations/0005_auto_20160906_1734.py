# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_maps', '0004_auto_20160825_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='objects',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('objectX', models.FloatField(null=True)),
                ('objectY', models.FloatField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('dis', models.FloatField(null=True)),
                ('reliability', models.IntegerField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='obstacle',
        ),
    ]
