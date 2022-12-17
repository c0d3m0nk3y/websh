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
    search_fields = [
        'name',
        'acronym',
    ]


class StageAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]


class TankAdmin(admin.ModelAdmin):
    search_fields = [
        'fuel',
    ]


admin.site.register(Engine, EngineAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Tank, TankAdmin)
