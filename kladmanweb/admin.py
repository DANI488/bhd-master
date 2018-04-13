from django.contrib import admin
from .models import GeoTag, KladMan


# Register your models here.

class GeoTagAdmin(admin.ModelAdmin):
    list_display = ('return_id', 'return_title', 'return_longitude', 'return_latitude', 'return_height', 'return_hash')
    list_display_links = ('return_title',)
    ordering = ('id',)


class KladManAdmin(admin.ModelAdmin):
    list_display = ('return_id', 'return_username')
    ordering = ('id',)


admin.site.register(GeoTag, GeoTagAdmin)
admin.site.register(KladMan, KladManAdmin)
#d