# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0002_creative_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creative',
            name='behance',
        ),
        migrations.RemoveField(
            model_name='creative',
            name='dribbble',
        ),
        migrations.RemoveField(
            model_name='creative',
            name='github',
        ),
        migrations.RemoveField(
            model_name='creative',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='creative',
            name='picture',
        ),
    ]
