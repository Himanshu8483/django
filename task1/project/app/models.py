from django.db import models

# Create your models here.

class Student(models.Model):
    s_no = models.IntegerField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    city = models.CharField(max_length=50)