from django.contrib import admin
from department.models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location',)


admin.site.register(Department, DepartmentAdmin)

