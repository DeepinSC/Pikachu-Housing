from django.contrib import admin
from provider.models import Provider


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Provider, ProviderAdmin)
