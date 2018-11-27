# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from distance.models import Distance


class DistanceAdmin(admin.ModelAdmin):
    list_display = ('house_id', 'department_id', 'distance')


admin.site.register(Distance, DistanceAdmin)

# Register your models here.
