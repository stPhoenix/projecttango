# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-11 20:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_remove_comment_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 11, 20, 30, 0, 324832, tzinfo=utc)),
        ),
    ]