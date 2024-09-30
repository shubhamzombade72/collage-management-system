from django.db import models

# Create your models here.
class students(models.Model):
    sid=models.CharField(max_length=255)
    sname=models.CharField(max_length=255)
    ssubject=models.CharField(max_length=255)
    ssubcode=models.CharField(max_length=255)
    sdepartment=models.CharField(max_length=255)
    smno=models.CharField(max_length=255)
    semail=models.CharField(max_length=255)
    smname=models.CharField(max_length=255)
    sfname=models.CharField(max_length=255)
    saddress=models.CharField(max_length=255)
    
    class Meta:
        db_table = 'tbl_student'
