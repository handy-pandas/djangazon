# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20170519_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='account_number',
            field=models.IntegerField(),
        ),
    ]
