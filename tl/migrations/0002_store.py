# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_no', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('test_store', models.BooleanField(default=0)),
                ('pair', models.IntegerField()),
            ],
        ),
    ]