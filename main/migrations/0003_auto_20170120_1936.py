# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170120_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slides',
            name='slide',
            field=models.ImageField(upload_to='slides'),
        ),
    ]