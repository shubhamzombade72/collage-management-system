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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),

    path('faculty-list/', facultyview.faculty1),
    path('student-list/',studentview.student1),

    path('sub-list/',subjectview.subject),
]
