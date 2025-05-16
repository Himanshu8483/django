from django.db import models

# Create your models here.
class Students(models.Model):
    stuname = models.CharField(max_length=50)
    stuemail = models.EmailField()  
    studetail = models.CharField(max_length=300)
    stuphone = models.BigIntegerField()  
    studob = models.DateField(null=True, blank=True)
    stuedu = models.CharField(max_length=50, null=True, blank=True)
    stugender = models.CharField(max_length=50, null=True, blank=True)

    stuimage = models.ImageField(upload_to='images/', blank=True, null=True)
    sturesume = models.FileField(upload_to='files/', blank=True, null=True)
    stupass = models.CharField(max_length=50)

    def __str__(self):
        return self.stuname  

class StuQuery(models.Model):
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField()
    title = models.CharField(max_length=255)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stuname