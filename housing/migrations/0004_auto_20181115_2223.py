# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0003_auto_20181114_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='imgs_url',
            field=django.contrib.postgres.fields.ArrayField(default=[], size=25, base_field=models.CharField(max_length=512, blank=True), blank=True),
        ),
    ]
