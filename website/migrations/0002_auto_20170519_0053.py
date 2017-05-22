# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='seller_id',
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='website.Category'),
            preserve_default=False,
        ),
    ]
