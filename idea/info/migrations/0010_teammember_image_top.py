# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-05-22 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image_top',
            field=models.ImageField(default='', upload_to=b''),
            preserve_default=False,
        ),
    ]
