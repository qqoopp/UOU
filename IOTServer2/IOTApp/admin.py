from django.contrib import admin
from IOTApp.models import *

# Register your models here.

# Setting admin title
admin.site.site_header = 'IOT Manage'
admin.site.site_title = 'IOT Manage:'


# Measureed data
class MeasureAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ['MeasureDT','EquipNo','ControllerNo','SensorNo','RcvDT','SndDT','Value']
    list_display_links = list_display
    search_fields = ['EquipNo','ControllerNo','SensorNo']

admin.site.register(tMeasure, MeasureAdmin)


