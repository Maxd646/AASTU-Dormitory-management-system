from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Staff, Student, Room

class StaffAdminSite(AdminSite):
    site_header = "Staff Admin"
    site_title = "Staff Admin Panel"
    index_title = "Welcome, Staff"

staff_admin_site = StaffAdminSite(name='staff_admin')

# Register Staff-specific models
staff_admin_site.register(Staff)
staff_admin_site.register(Student)
staff_admin_site.register(Room)
