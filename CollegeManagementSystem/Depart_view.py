from django.shortcuts import render,redirect
from django.http import response
from Departments.models import Department

def department_list(request):
    department_data = Department.objects.all()
    data = {
        "department_data": department_data
    }
    return render(request, 'Departments/index.html', data)

def department_view(request, id):
    department_data = Department.objects.all()  
    data = {
        "department_data": department_data,
        "id": int(id),  
    }
    return render(request,"Departments/view.html",data)



def add_department(request):
    if request.method == 'GET':
        return render(request, "Departments/departadd.html")
    else:
        dept_name = request.POST.get("dept_name")
        dept_code = request.POST.get("dept_code")
        hod_name = request.POST.get("hod_name")
        dept_location = request.POST.get("dept_location")
        contact_number = request.POST.get("contact_number")
        email_address = request.POST.get("email_address")

        save_data = Department(
            dept_name=dept_name,
            dept_code=dept_code,
            hod_name=hod_name,
            dept_location=dept_location,
            contact_number=contact_number,
            email_address=email_address,
        )
        save_data.save()
        return redirect(department_list)

def edit_department(request, id):
    department_data = Department.objects.get(id=int(id))
    
    if request.method == 'GET':
        data = {
            "department_data": department_data
        }
        return render(request, "Departments/departedit.html", data)
    
    else:
        dept_name = request.POST.get("dept_name")
        dept_code = request.POST.get("dept_code")
        hod_name = request.POST.get("hod_name")
        dept_location = request.POST.get("dept_location")
        contact_number = request.POST.get("contact_number")
        email_address = request.POST.get("email_address")

        department_data.dept_name = dept_name
        department_data.dept_code = dept_code
        department_data.hod_name = hod_name
        department_data.dept_location = dept_location
        department_data.contact_number = contact_number
        department_data.email_address = email_address

        department_data.save()
        return redirect(department_list)

def delete_department(request,id):
    department = Department.objects.get(id=int(id))
    department.delete()
    return redirect(department_list)

def LoginForm(request):
    if request.method == "GET":
        return render(request,"Department/loginForm.html")
    else:
        email = request.POST.get("femail")
        password = request.POST.get("password")

        saveData = department_list(
            femail=email,
            password=password,
            )
        saveData.save()
        return redirect(department_list)
