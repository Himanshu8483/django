from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    active = models.BooleanField(default=True) 

    
    def __str__(self):
        return self.name