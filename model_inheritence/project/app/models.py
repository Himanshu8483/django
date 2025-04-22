from django.db import models

# Create your models here.
class BaseField(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact= models.IntegerField()
    class Meta:
        abstract = True
class Student(BaseField):
    course = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    fees= models.IntegerField()
    def __str__(self):
        return self.name
    
class Employee(BaseField):
    contact = None
    department = models.CharField(max_length=50)
    emp_id= models.IntegerField()
    salary = models.IntegerField()
    
class Client(BaseField):
    project= models.IntegerField()
    billing_status = models.CharField(max_length=50)