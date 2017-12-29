# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-29 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_case_visual_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='visual_text',
        ),
        migrations.AddField(
            model_name='case',
            name='pictures_editor',
            field=models.TextField(blank=True, null=True, verbose_name='pictures_editor'),
        ),
    ]
