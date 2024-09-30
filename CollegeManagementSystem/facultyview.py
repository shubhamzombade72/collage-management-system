from django.shortcuts import render,redirect
from Faculty.models import facultys
def faculty1(request):
    facultyData = facultys.objects.all()
    fdatadata={
        "facultyData":facultyData
    }
    return render(request,"Faculty/index.html",fdatadata)


def facultyview(request,id):
    facultyData = facultys.objects.all()
  
    fdata={
        "facultyData":facultyData,
         "id":int(id),
    }
    return render(request,"Faculty/view.html",fdata)

def delete(request,id):
    customerData= facultys.objects.get(id=int(id))
    customerData.delete() 
    return redirect(faculty1)