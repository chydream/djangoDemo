# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-08 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id_no',
            field=models.CharField(default='1', max_length=10, verbose_name='学号'),
        ),
    ]
