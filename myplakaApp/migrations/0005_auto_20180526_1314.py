# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-26 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myplakaApp', '0004_bildirim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildirim',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bildirim', to='myplakaApp.Search'),
        ),
    ]
