from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class BaseInfo(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    fees = models.IntegerField()
    class Meta:         # for changing behaviour of class
        verbose_name= "MyCustomModel"       # table name with automatic s  show in admin browser
        # verbose_name_plural = "MyCustomModel"   # without s 
        db_table = 'Student'        # show in db.sqlite
        ordering = ['-name']        # - for reverse order
        ordering = ['address']
    
    def __str__(self):
        return self.name

    
class ProxyBaseInfo(BaseInfo):
    class Meta:
        proxy = True
    def __str__(self):
        return self.name
