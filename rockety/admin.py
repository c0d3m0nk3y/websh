from django.contrib import admin

from .models import *


class EngineAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_fuels',
        'isp',
    ]
    search_fields = [
        'name',
    ]

    def get_fuels(self, obj):
        return obj.get_fuels()

    get_fuels.short_description = "Fuels"


class FuelAdmin(admin.ModelAdmin):
    list_display = [
        'acronym',
        'name',
    ]
    search_fields = [
        'name',
        'acronym',
    ]


class StageAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]


class TankAdmin(admin.ModelAdmin):
    list_display = [
        'get_name',
        'fuel',
    ]
    search_fields = [
        'fuel',
    ]

    def get_name(self, obj):
        return str(obj)

    get_name.short_description = "Tank"


admin.site.register(Engine, EngineAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Tank, TankAdmin)
