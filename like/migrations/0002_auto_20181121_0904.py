# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0007_auto_20181116_2103'),
        ('users', '0001_initial'),
        ('like', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('house_id', models.ForeignKey(related_name='liked_house', to='housing.House')),
                ('user_id', models.ForeignKey(related_name='liked_user', to='users.UserProfile')),
            ],
        ),
        migrations.DeleteModel(
            name='Provider',
        ),
    ]
