from django.shortcuts import render,redirect
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

def delete(request,id):
    StudentData= students.objects.get(id=int(id))
    StudentData.delete() 
    return redirect(student1)


def editstudent(request,id):
    StudentData= students.objects.get(id=int(id))
    if request.method == "GET":
        sdata={
        "StudentData":StudentData,
    }
        return render(request,"student/edit.html",sdata)
    else:
        name = request.POST.get("sname")
        department = request.POST.get("sdepartment")
        mno = request.POST.get("smno")
        email = request.POST.get("semail")
        mname= request.POST.get("smname")
        fname= request.POST.get("sfname")
        address= request.POST.get("saddress")

        StudentData.sname=name
        StudentData.sdepartment=department
        StudentData.smno=mno
        StudentData.semail=email
        StudentData.smname=mname
        StudentData.sfname=fname
        StudentData.saddress=address
        StudentData.save()
        return redirect(student1)
    

def Addstudent(request):
    if request.method == "GET":
        return render(request,"student/addform.html")
    else:
        name = request.POST.get("sname")
        department = request.POST.get("sdepartment")
        mno = request.POST.get("smno")
        email = request.POST.get("semail")
        mname= request.POST.get("smname")
        fname= request.POST.get("sfname")
        address= request.POST.get("saddress")


        saveData = students(
            sname=name,
            sdepartment=department,
            smno=mno,
            semail=email,
            smname=mname,
            sfname=fname,
            saddress=address
            )
        saveData.save()
        return redirect(student1)
    
def LoginForm(request):
    if request.method == "GET":
        return render(request,"student/loginform.html")
    else:
        email = request.POST.get("femail")
        password = request.POST.get("password")

        saveData = students(
            femail=email,
            password=password,
            )
        saveData.save()
        return redirect(student1)
    
    


