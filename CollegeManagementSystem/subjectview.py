from django.shortcuts import render,redirect
from django.http import response
from subject.models import Subjects
def subject(request):
    subData = Subjects.objects.all()
    if not request.session.get("success"): 
        subData={
            "subData":subData
        }
    else:
        message = request.session.get("success")
        subData={
            "subData":subData,
            "Message":message
        }
        del request.session["success"]
    return render(request,"subjects/index.html",subData)

def view(request,id):
    subData= Subjects.objects.get(id=id)
    print(id)
    data = {
        "subData":subData,
        "id":int(id)
    }
    return render(request,'subjects/view.html',data)


def delete(request,id):
    subData= Subjects.objects.get(id=int(id))
    subData.delete() 
    return redirect(subject)

def edit(request,id):
    subData= Subjects.objects.get(id=int(id))
    if request.method == "GET":
        subData={
        "subData":subData,
    }
        return render(request,"subjects/edit.html",subData)
    else:
        name = request.POST.get("subname")
        cod = request.POST.get("sub_code")
        dept= request.POST.get("sub_dept")
        sem = request.POST.get("sem")
        subData.subname=name
        subData.sub_code=cod
        subData.sub_dept=dept
        subData.sem=sem
        subData.save()
        return redirect(subject)
    

def Addsubject(request):
    if request.method == "GET":
        return render(request,"subjects/addform.html")
    else:
        name = request.POST.get("subname")
        cod = request.POST.get("sub_code")
        dept= request.POST.get("sub_dept")
        sem = request.POST.get("sem")
        #pass models classs (eg.Subjects)
        saveData = Subjects( 
            subname=name,
            sub_code=cod,
            sub_dept=dept,
            sem=sem,
            )
        saveData.save()
        
        request.session["success"] = "Record added successfully!"
        return redirect(subject)