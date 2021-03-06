# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-23 21:20
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20180121_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_list_four',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_list_four'),
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_list_one',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_list_one'),
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_list_three',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_list_three'),
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_list_two',
            field=redactor.fields.RedactorField(blank=True, verbose_name='service_list_two'),
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_title_four',
            field=models.CharField(default='', max_length=255, verbose_name='service_title_four'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_title_one',
            field=models.CharField(default='', max_length=255, verbose_name='service_title_one'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_title_three',
            field=models.CharField(default='', max_length=255, verbose_name='service_title_three'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexpageinfoct',
            name='service_title_two',
            field=models.CharField(default='', max_length=255, verbose_name='service_title_two'),
            preserve_default=False,
        ),
    ]
