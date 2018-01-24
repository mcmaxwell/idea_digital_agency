# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-23 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0008_auto_20180124_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationcontent',
            name='urlconf_path',
            field=models.CharField(choices=[(b'cases.urls', b'Cases category'), (b'blog.urls', b'Blog application'), (b'info.urls', b'Info app')], max_length=100, verbose_name='application'),
        ),
        migrations.AlterField(
            model_name='indexpageinfoct',
            name='title',
            field=redactor.fields.RedactorField(verbose_name='title'),
        ),
    ]