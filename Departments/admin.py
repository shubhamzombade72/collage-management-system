from django.contrib import admin
from Departments.models import Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_code', 'hod_name', 'dept_location', 'contact_number', 'email_address')

admin.site.register(Department, DepartmentAdmin)
