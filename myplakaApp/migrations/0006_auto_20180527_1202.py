# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-27 12:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myplakaApp', '0005_auto_20180526_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bildirim',
            old_name='mesaj',
            new_name='content',
        ),
    ]