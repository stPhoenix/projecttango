# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-28 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='image_url',
            field=models.URLField(default='media/article_images/default.jpg'),
        ),
    ]
