# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_student_s_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_content', tinymce.models.HTMLField()),
                ('b_author', models.CharField(max_length=32)),
            ],
        ),
    ]