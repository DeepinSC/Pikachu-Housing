# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    #replaces = [(b'department', '0001_initial'), (b'department', '0002_auto_20181111_1933'), (b'department', '0003_auto_20181111_1938'), (b'department', '0004_auto_20181111_1939'), (b'department', '0005_auto_20181111_1946'), (b'department', '0006_auto_20181111_1950'), (b'department', '0007_auto_20181111_1951'), (b'department', '0008_auto_20181111_2008'), (b'department', '0009_auto_20181112_0014'), (b'department', '0010_auto_20181112_0025'), (b'department', '0011_auto_20181112_0030'), (b'department', '0012_auto_20181112_0030')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('latitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
            ],
        ),
    ]
