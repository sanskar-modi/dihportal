# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160617_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='team_leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_team_leader', to='projects.Student'),
        ),
    ]
