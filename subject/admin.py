from django.contrib import admin
from subject.models import Subjects
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display=('subname','sub_code','sub_dept','sem',)
admin.site.register(Subjects,SubjectAdmin)

    

