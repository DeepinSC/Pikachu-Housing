# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('url', models.CharField(max_length=128, blank=True)),
                ('email', models.CharField(max_length=128, blank=True)),
                ('phone', models.CharField(max_length=128, blank=True)),
            ],
        ),
    ]
