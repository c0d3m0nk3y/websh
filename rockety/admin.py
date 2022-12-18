from django.contrib import admin
from django.db.models import Q

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


class RocketAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'get_stages',
        'get_dry_mass',
        'get_wet_mass',
    ]

    def get_stages(self, obj):
        return obj.get_stages()
    get_stages.short_description = "Stages"

    def get_dry_mass(self, obj):
        return f"{obj.dry_mass:,.2f}"
    get_dry_mass.short_description = "Dry Mass (kg)"

    def get_wet_mass(self, obj):
        return f"{obj.wet_mass:,.2f}"
    get_wet_mass.short_description = "Wet Mass (kg)"


class StageAdmin(admin.ModelAdmin):
    search_fields = [
        'name',
    ]


class TankAdmin(admin.ModelAdmin):
    list_display = [
        'get_name',
        'fuel',
        'get_volume',
        'get_capacity',
    ]
    search_fields = [
        'name',
    ]

    def get_name(self, obj):
        return str(obj)
    get_name.short_description = "Tank"

    def get_volume(self, obj):
        return f"{obj.volume:,.2f}"
    get_volume.short_description = "Volume (m³)"

    def get_capacity(self, obj):
        return f"{obj.capacity:,.2f}"
    get_capacity.short_description = "Capacity (kg)"

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term
        )

        if "to" in search_term:
            a, b = search_term.replace(',','').split('to')
            queryset |= self.model.objects.filter(
                Q(volume__range=[a, b])
                | Q(capacity__range=[a, b])
            )

        return queryset, may_have_duplicates


admin.site.register(Engine, EngineAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Stage, StageAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(Rocket, RocketAdmin)
