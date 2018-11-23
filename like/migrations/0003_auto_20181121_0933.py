# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_auto_20181121_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(related_name='liked_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
