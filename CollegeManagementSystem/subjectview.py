from django.shortcuts import render
from subject.models import Subjects
def subject(request):
    subData = Subjects.objects.all()
    subData={
        "subData":subData
    }
    return render(request,"subjects/index.html",subData)

def view(request,id):
    subData= Subjects.objects.all()
    print(id)
    data = {
        "subData":subData,
        "id":int(id)
    }
    return render(request,'subjects/view.html',data)