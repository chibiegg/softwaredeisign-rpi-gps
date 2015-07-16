# encoding=utf-8

from django.contrib import admin
from gpsnow.models import Transponder, Waypoint

class TransponderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")

admin.site.register(Transponder, TransponderAdmin)


class WaypointAdmin(admin.ModelAdmin):
    list_display = ("id", "transponder", "created", "latitude", "longitude")
    filter_fields = ("transponder",)

admin.site.register(Waypoint, WaypointAdmin)
