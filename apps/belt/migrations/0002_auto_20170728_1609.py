# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 21:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='users',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
