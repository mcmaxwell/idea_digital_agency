# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-29 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0005_auto_20171229_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='visual_text',
            field=models.TextField(blank=True, null=True, verbose_name='visual_text'),
        ),
    ]
