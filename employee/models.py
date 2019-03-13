from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=100)
    emp_designation = models.CharField(max_length=50)
    emp_contact = models.CharField(max_length=20)
    emp_email = models.CharField(max_length=20)
    class Meta:
        db_table = "employee"
