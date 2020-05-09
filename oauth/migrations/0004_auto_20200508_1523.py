# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-08 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0003_auto_20200508_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='课程名称')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProxyStudent',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('oauth.student',),
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-updated_at'], 'verbose_name': '学生表', 'verbose_name_plural': '学生表'},
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='oauth.Course'),
        ),
    ]