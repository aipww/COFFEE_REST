# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-11 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pas', models.CharField(max_length=100)),
            ],
        ),
    ]
