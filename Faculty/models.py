from django.db import models

# Create your models here.
class facultys(models.Model):
    fid=models.CharField(max_length=255)
    fname=models.CharField(max_length=255)
    fh_name=models.CharField(max_length=255)
    fmno=models.CharField(max_length=255)
    femail=models.CharField(max_length=255)
    fdepartment=models.CharField(max_length=255)
    fposition=models.CharField(max_length=255)
    fqualification=models.CharField(max_length=255)
    class Meta:
        db_table = 'tbl_Faculty'
