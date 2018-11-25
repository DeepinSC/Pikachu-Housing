# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0007_auto_20181116_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='closest_department_float',
            field=models.FloatField(default=-1, null=True, blank=True),
        ),
    ]
