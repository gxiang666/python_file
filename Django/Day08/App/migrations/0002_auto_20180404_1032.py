# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='g_position',
            field=models.CharField(default='1教室', max_length=32),
        ),
        migrations.AddField(
            model_name='grade',
            name='g_student_count',
            field=models.IntegerField(default=30),
        ),
    ]
