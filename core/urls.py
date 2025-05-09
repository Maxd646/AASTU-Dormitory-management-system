from django.contrib import admin
from django.urls import path, include
# from Dorm_management_system.proctor_admin import proctor_admin_site
# from Dorm_management_system. staff_admin import staff_admin_site


urlpatterns = [
    path('admin/', admin.site.urls),                # Superuser panel
    # cd "C:\Users\hp\Downloads\DormitoryManagement\Dormiratry management syatem"

    path("", include("apps.home.urls")),  # Home page
]
