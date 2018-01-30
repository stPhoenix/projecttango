# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-30 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybb', '0009_account_accountdeletion_emailaddress_emailconfirmation_passwordexpiry_passwordhistory_signupcode_sig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='autosubscribe',
            field=models.BooleanField(default=False, help_text='Automatically subscribe to topics that you answer', verbose_name='Automatically subscribe'),
        ),
    ]
