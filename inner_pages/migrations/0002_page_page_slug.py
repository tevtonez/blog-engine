# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inner_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_slug',
            field=models.CharField(default='page-', max_length=20, unique=True),
        ),
    ]
