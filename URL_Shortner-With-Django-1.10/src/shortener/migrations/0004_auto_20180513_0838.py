# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-13 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_myurl_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
