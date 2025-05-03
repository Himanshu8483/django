from django.db import models

class Department(models.Model):
    dep_name = models.CharField(unique=True)  # Must be unique if used in to_field
    dep_dis = models.CharField(max_length=100)
    dep_hod = models.CharField(max_length=20)

    def __str__(self):
        return self.dep_name

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(unique=True)
    stu_contact = models.IntegerField()
    stu_dep = models.ForeignKey(
        Department,
        to_field='dep_name',  # Reference by dep_name instead of id
        on_delete=models.PROTECT,
        related_name='students'
    )

    def __str__(self):
        return f"{self.stu_name} - {self.stu_dep.dep_name}"
