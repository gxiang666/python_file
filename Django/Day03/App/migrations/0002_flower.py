# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'Flower',
            },
        ),
    ]
