from django.shortcuts import render
from subject.models import Subjects
def subject(request):
    subData = Subjects.objects.all()
    subData={
        "subData":subData
    }
    return render(request,"subjects/index.html",subData)