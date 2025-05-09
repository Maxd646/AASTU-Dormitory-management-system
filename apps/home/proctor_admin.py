from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Proctor, Building, Room

class ProctorAdminSite(AdminSite):
    site_header = "Proctor Admin"
    site_title = "Proctor Admin Panel"
    index_title = "Welcome, Proctor"

proctor_admin_site = ProctorAdminSite(name='proctor_admin')

# Register Proctor-specific models
proctor_admin_site.register(Proctor)
proctor_admin_site.register(Building)
proctor_admin_site.register(Room)
