# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-18 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartdice',
            name='mode',
            field=models.CharField(default='D6', max_length=20),
        ),
        migrations.AlterField(
            model_name='rollresult',
            name='value',
            field=models.CharField(max_length=200),
        ),
    ]
