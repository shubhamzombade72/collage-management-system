from django.shortcuts import render,redirect
from Departments.models import Department

def department_list(request):
    department_data = Department.objects.all()
    data = {
        "department_data": department_data
    }
    return render(request, 'Departments/index.html', data)

# def department_view(request, id):
#     department_data = Department.objects.get(id=int(id))
#     data = {
#         'department_data': department_data,
#         'Id': int(id)
#     }
#     return render(request, 'department/view.html', data)

def add_department(request):
    if request.method == 'GET':
        return render(request, "department/department_form.html")
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

# def edit_department(request, id):
#     department = Department.objects.get(id=int(id))
    
#     if request.method == 'GET':
#         data = {
#             "department": department
#         }
#         return render(request, "department/department_edit.html", data)
    
#     else:
#         dept_name = request.POST.get("dept_name")
#         dept_code = request.POST.get("dept_code")
#         hod_name = request.POST.get("hod_name")
#         dept_location = request.POST.get("dept_location")
#         contact_number = request.POST.get("contact_number")
#         email_address = request.POST.get("email_address")

#         department.dept_name = dept_name
#         department.dept_code = dept_code
#         department.hod_name = hod_name
#         department.dept_location = dept_location
#         department.contact_number = contact_number
#         department.email_address = email_address

#         department.save()
#         return redirect(department_list)

# def delete_department(request, id):
#     department = Department.objects.get(id=int(id))
#     department.delete()
#     return redirect(department_list)
