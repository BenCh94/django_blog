# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging_app', '0002_auto_20160712_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]