# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-29 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171228_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtag',
            name='tag_en',
            field=models.CharField(max_length=255, null=True, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='tag_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='tag'),
        ),
        migrations.AddField(
            model_name='blogtag',
            name='tag_uk',
            field=models.CharField(max_length=255, null=True, verbose_name='tag'),
        ),
    ]
