# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20181112_0104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='imgs',
            new_name='imgs_url',
        ),
    ]
