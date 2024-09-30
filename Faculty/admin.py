from django.contrib import admin
from Faculty.models import facultys
# Register your models here.
class FacultyAdmin(admin.ModelAdmin):
    list_display=("fid","fname","fh_name","fmno","femail","fdepartment","fposition","fqualification",)
admin.site.register(facultys,FacultyAdmin)