from django.shortcuts import render,redirect
from Faculty.models import facultys
def faculty1(request):
    facultyData = facultys.objects.all()
    fdata={
        "facultyData":facultyData
    }
    return render(request,"Faculty/index.html",fdata)


def fview(request, id):
    facultyData = facultys.objects.all()  
    fdata = {
        "facultyData": facultyData,
        "id": int(id),  
    }
    return render(request,"Faculty/view.html",fdata)

def delete(request,id):
    facultyData= facultys.objects.get(id=int(id))
    facultyData.delete() 
    return redirect(faculty1)

def editFaculty(request,id):
    facultyData= facultys.objects.get(id=int(id))
    if request.method == "GET":
        fdata={
        "facultyData":facultyData,
    }
        return render(request,"Faculty/edit.html",fdata)
    else:
        name = request.POST.get("fname")
        hodname = request.POST.get("fh_name")
        mno= request.POST.get("fmno")
        email = request.POST.get("femail")
        dept = request.POST.get("fdepartment")
        positions = request.POST.get("fposition")
        qualify= request.POST.get("fqualification")
        facultyData.fname=name
        facultyData.fh_name=hodname
        facultyData.fmno=mno
        facultyData.femail=email
        facultyData.fdepartment=dept
        facultyData.fposition=positions
        facultyData.fqualification=qualify
        facultyData.save()
        return redirect(faculty1)
    

def AddFaculty(request):
    if request.method == "GET":
        return render(request,"Faculty/addform.html")
    else:
        name = request.POST.get("fname")
        hodname = request.POST.get("fh_name")
        mno= request.POST.get("fmno")
        email = request.POST.get("femail")
        dept = request.POST.get("fdepartment")
        positions = request.POST.get("fposition")
        qualify= request.POST.get("fqualification")

        saveData = facultys(
            fname=name,
            fh_name=hodname,
            fmno=mno,
            femail=email,
            fdepartment=dept,
            fposition=positions,
            fqualification=qualify,
            )
        saveData.save()
        return redirect(faculty1)