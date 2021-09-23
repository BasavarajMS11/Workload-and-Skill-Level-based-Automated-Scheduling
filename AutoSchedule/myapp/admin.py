from django.contrib import admin
#from .models import usersLog
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#admin.site.register(usersLog)
admin.site.register(CSV)

@admin.register(Months, Machines)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(Employees)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(MPPMarch1s, MPPMarch2s)
class MPPAdmin(ImportExportModelAdmin):
    exclude = ('id', )

@admin.register(Manpowers, Schedules)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )


