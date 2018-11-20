# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=128, blank=True)),
                ('price', models.IntegerField(default=0)),
                ('types', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=600, blank=True)),
                ('provider', models.ForeignKey(blank=True, to='provider.Provider', null=True)),
                ('cover_img', models.CharField(default=b'', max_length=128, blank=True)),
                ('imgs', django.contrib.postgres.fields.ArrayField(default=[], size=100, base_field=models.CharField(max_length=128, blank=True), blank=True)),
                ('latitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.FloatField(default=0, null=True, blank=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
            ],
        ),
    ]
