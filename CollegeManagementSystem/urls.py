"""
URL configuration for CollegeManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CollegeManagementSystem import views
from CollegeManagementSystem import facultyview
from CollegeManagementSystem import studentview
from CollegeManagementSystem import subjectview
from CollegeManagementSystem import Depart_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),

    



    path('student-list/',studentview.student1),
    path('student-view/<id>',studentview.sview),
    path('student-delete/<id>',studentview.delete),
    path('student-edit/<id>',studentview.editstudent),
    path('student-add/',studentview.Addstudent),
    path('student/',studentview.LoginForm),





    path('faculty-list/', facultyview.faculty1),
    path('faculty-view/<id>', facultyview.fview),
    path('faculty-delete/<id>',facultyview.delete),
    path('faculty-edit/<id>', facultyview.editFaculty),
    path('faculty-add/', facultyview.AddFaculty),

    


    

    path('department-list/', Depart_view.department_list),
    path('department-add/', Depart_view.add_department),
    path('department-edit/<id>', Depart_view.edit_department),  
    path('department-view/<id>', Depart_view.department_view),
    path('department-delete/<id>', Depart_view.delete_department),







    path('sub-list/',subjectview.subject),
    path('sub-view/<id>',subjectview.view),
    path('sub-edit/<id>',subjectview.edit),
    path('sub-add/',subjectview.Addsubject),
    path('sub-delete/<id>',subjectview.delete),

]
