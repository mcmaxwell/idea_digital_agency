# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-10 01:01
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_auto_20180109_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='seo_description',
            field=redactor.fields.RedactorField(blank=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='seo_keywords',
            field=redactor.fields.RedactorField(blank=True),
        ),
    ]
