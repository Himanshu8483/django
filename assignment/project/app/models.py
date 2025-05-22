from django.db import models
from datetime import date

# Q1 
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
    
    
class Offer(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    def is_eligible(self):
        today = date.today()
        return self.start_date <= today <= self.end_date

class Discount(Offer):
    name = models.CharField(max_length=100)
    percentage = models.FloatField()

class Promotion(Offer):
    title = models.CharField(max_length=100)
    description = models.TextField()



# Q2 

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField()

class OrderedBook(Book):
    class Meta:
        proxy = True
        ordering = ['-published_date']  # Descending order

class FormattedBook(Book):
    class Meta:
        proxy = True

    def formatted_details(self):
        return f"{self.title} - {self.published_date}"

class RecentBook(Book):
    class Meta:
        proxy = True

    def is_recent(self):
        today = date.today()
        return self.published_date.year == today.year or self.published_date.year == today.year - 1

        # return self.published_date.year in [today.year, today.year - 1]

