# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0003_auto_20181121_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='has_liked',
            field=models.BooleanField(default=True),
        ),
    ]
