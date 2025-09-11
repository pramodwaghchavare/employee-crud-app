from django.db import models

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    email_id = models.EmailField(max_length=100, unique=True)
    age = models.IntegerField(null=True, blank=True)  # New field for age
    selectedGender = models.CharField(max_length=10, null=True, blank=True)  # New field for
    dob = models.DateField(null=True, blank=True)  # New field for date of birth
    skills = models.TextField(null=True, blank=True)  # New field for skills
    class Meta:
        db_table = 'employees'  # 👈 tells Django to use the existing table
        managed = False         # 👈 don't let Django create or modify it

