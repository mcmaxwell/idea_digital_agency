# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-28 23:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogtag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='insta_link',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tele_link',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='twitter_link',
        ),
    ]
