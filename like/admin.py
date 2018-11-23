from django.contrib import admin

from like.models import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'house_id',)


admin.site.register(Like, LikeAdmin)
