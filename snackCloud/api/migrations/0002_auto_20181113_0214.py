# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-13 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='ProductID',
        ),
        migrations.AddField(
            model_name='sale',
            name='InventoryID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Inventory'),
            preserve_default=False,
        ),
    ]
