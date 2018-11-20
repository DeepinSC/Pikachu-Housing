# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0004_auto_20181115_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='cover_img',
            field=models.CharField(default=b'', max_length=512, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.CharField(max_length=1024, blank=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(max_length=128),
        ),
    ]
