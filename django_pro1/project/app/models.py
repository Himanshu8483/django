from django.db import models

# Create your models here.

class Students(models.Model):
    stuname     =   models.CharField(max_length=50)
    stuemial    =   models.EmailField()
    studetails  =   models.CharField(max_length=300)
    stuphone    =   models.IntegerField()
    studob      =   models.DateField()
    stuedu      =   models.CharField(max_length=50)
    stugender   =   models.CharField(max_length=50)
    stuimage    =   models.ImageField(upload_to='image/')
    sturesume   =   models.FileField(upload_to='file/')
    stupass     =   models.CharField(max_length=50)
