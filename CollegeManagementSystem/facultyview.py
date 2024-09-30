from django.shortcuts import render
from Faculty.models import facultys
def faculty1(request):
    facultyData = facultys.objects.all()
    fdatadata={
        "facultyData":facultyData
    }
    return render(request,"Faculty/index.html",fdatadata)
