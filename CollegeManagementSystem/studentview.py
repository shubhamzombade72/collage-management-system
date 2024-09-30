from django.shortcuts import render
from student.models import students
def student1(request):
    StudentData = students.objects.all()
    sdata={
        "StudentData":StudentData
    }
    return render(request,"student/index.html",sdata)
