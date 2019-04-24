# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16, unique=True)),
                ('u_age', models.IntegerField(default=1)),
                ('u_password', models.CharField(max_length=32)),
                ('u_token', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
    ]
