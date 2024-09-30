from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=255) 
    dept_code = models.CharField(max_length=255)  
    hod_name = models.CharField(max_length=255)   
    dept_location = models.CharField(max_length=255)  
    contact_number = models.CharField(max_length=255)  
    email_address = models.CharField(max_length=255)  

    class Meta:
        db_table = 'tbl_department'  

   
