from django.db import models
from datetime import date

class Person(models.Model):
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age

class Student(Person):
    name= models.CharField(max_length=50)
    
    
class Teacher(Person):
    name= models.CharField(max_length=50)