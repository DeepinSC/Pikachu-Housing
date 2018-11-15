# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from housing.models import House
from department.models import Department

# Create your models here.

class Distance(models.Model):
    house_id = models.ForeignKey(House, blank=False, null=False, related_name='distance', on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, blank=False, null=False, related_name='distance', on_delete=models.CASCADE)
    distance = models.FloatField(default=0, blank=False)