# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-28 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171228_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtag',
            name='blog',
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(to='blog.BlogTag'),
        ),
    ]
