from django.shortcuts import render
from student.models import students
def student1(request):
    StudentData = students.objects.all()
    sdata={
        "StudentData":StudentData
    }
    return render(request,"student/index.html",sdata)

def sview(request,id):
    StudentData = students.objects.all()
    print(id)
    sdata={
        "StudentData":StudentData,
        "id":int(id),
    }
    return render(request,"student/view.html",sdata)

