from django.db import models

# Create your models here.
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
        return self.stuname  
