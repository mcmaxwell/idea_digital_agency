# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-21 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0006_auto_20180116_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpageinfoct',
            name='sub_title',
            field=models.CharField(default='', max_length=255, verbose_name='sub_title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
    ]