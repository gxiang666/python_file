# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-28 03:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_flower_f_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='a_leg',
            new_name='a_legs',
        ),
    ]