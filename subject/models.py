from django.db import models

# Create your models here.

class Subjects(models.Model):
    subname=models.CharField(max_length=255)
    sub_code=models.CharField(max_length=155)
    sub_dept=models.CharField(max_length=255)
    sem=models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_subject'