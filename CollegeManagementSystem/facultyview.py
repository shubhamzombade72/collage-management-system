from django.shortcuts import render,redirect
from Faculty.models import facultys
from django.http import response

def faculty1(request):
    facultyData = facultys.objects.all()
    if not request.session.get("success"):
        fdata={
            "facultyData":facultyData,
        }
    else:
        message = request.session.get("success")
        fdata={
            "facultyData":facultyData,
            "Message": message
        }
        del request.session["success"]

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
         
        request.session["success"] = "Record added successfully!"
        return redirect(faculty1)
        
    
def LoginForm(request):
    if request.method == "GET":
        return render(request, "Faculty/LoginForm.html")
    else:
        email = request.POST.get("femail")
        password = request.POST.get("password")

        # Verify if the faculty exists with the entered credentials
        try:
            facultyData = facultys.objects.get(femail=email, password=password)
            
            # Store user details in session
            request.session['faculty_id'] = facultyData.id
            request.session['faculty_name'] = facultyData.fname
            
            return redirect(faculty1)  # Redirect to the faculty dashboard
        except facultys.DoesNotExist:
            return render(request, "Faculty/LoginForm.html", {
                "error": "Invalid email or password"
            })