# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField(default='1996-02-11')),
                ('mobile', models.CharField(default='0', max_length=10)),
            ],
        ),
    ]
