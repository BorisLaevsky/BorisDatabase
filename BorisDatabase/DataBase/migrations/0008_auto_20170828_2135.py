# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0007_auto_20170828_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='DataBase.Company'),
        ),
    ]
