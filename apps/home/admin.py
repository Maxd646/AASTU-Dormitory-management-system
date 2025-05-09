
from django.contrib import admin

from django.contrib import admin
from .models import Proctor, Building, Room, Staff, Student, MaintenanceTeam, ProblemReport

admin.site.site_title = 'AASTU Dormitory Management System'  
admin.site.site_header = 'AASTU Dormitory Management System'   
admin.site.index_title = 'Welcome to AASTU Dormitory Admin'

class ProctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'phone')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'phone')

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'gender', 'proctor')

admin.site.register(Proctor, ProctorAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Room)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Student)
admin.site.register(MaintenanceTeam)
admin.site.register(ProblemReport)
