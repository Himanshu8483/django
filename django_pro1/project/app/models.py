from django.db import models

class Students(models.Model):
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField()  
    studetails = models.CharField(max_length=300)
    stuphone = models.BigIntegerField()  
    studob = models.DateField()
    stuedu = models.CharField(max_length=50)
    stugender = models.CharField(max_length=50)
    stuimage = models.ImageField(upload_to='images/', blank=True, null=True)
    sturesume = models.FileField(upload_to='files/', blank=True, null=True)
    stupass = models.CharField(max_length=50)

    def __str__(self):
        return self.stuname  # Return student's name when displayed

class Book(models.Model):
    student_name = models.CharField(max_length=100)
    clas = models.IntegerField()     
    section = models.CharField(max_length=1)
    book_title = models.CharField(max_length=100)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.book_title  # for better read
