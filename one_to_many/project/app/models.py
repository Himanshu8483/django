from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(unique = True)
    dep_dis =  models.CharField(max_length=100)
    dep_hod =  models.CharField(max_length=20)
    def __str__(self):
        return str(self.dep_name)

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(max_length=254,unique=True)
    stu_contact = models.IntegerField()
    stu_dep = models.ForeignKey(Department, on_delete=models.PROTECT) 
    def __str__(self):
        return self.stu_name+' '+str(self.stu_email)