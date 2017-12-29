# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-29 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='project',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='case',
            name='project_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='case',
            name='project_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='case',
            name='project_uk',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='project'),
        ),
    ]
