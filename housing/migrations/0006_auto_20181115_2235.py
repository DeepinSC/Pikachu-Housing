# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0005_auto_20181115_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='types',
            field=models.CharField(max_length=64, blank=True),
        ),
    ]
