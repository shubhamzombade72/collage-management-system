from django.contrib import admin
from student.models import students

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display=("sid","sname","sdepartment","smno","semail","smname","sfname","saddress")
admin.site.register(students,studentAdmin)