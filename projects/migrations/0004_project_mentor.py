# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20160617_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.Mentor'),
            preserve_default=False,
        ),
    ]
