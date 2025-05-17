from django.db import models

# Create your models here.
class Students(models.Model):
    stuname=models.CharField(max_length=50)
    stuemail = models.EmailField()  
    
    def __str__(self):
        return self.stuname