from django.db import models

# Create your models here.
class Buy(models.Model):
    name= models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    number = models.IntegerField()
    payment = models.CharField(max_length=50)

    def __str__(self):
        return self.name