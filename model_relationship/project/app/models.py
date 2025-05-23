from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar_no = models.IntegerField(unique = True)
    created_by =  models.CharField(max_length=50)
    alloted_date =  models.DateTimeField()
    def __str__(self):
        return str(self.aadhar_no)  # object form return if comment str function(magic function)

class Citizen(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,unique=True)
    contact = models.IntegerField()
    aadhar_no = models.OneToOneField(Aadhar, on_delete=models.CASCADE, to_field='aadhar_no', related_name = "xyz") 
    def __str__(self):
        return self.name+' '+str(self.aadhar_no)