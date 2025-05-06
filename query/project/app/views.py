from django.shortcuts import render
from .models import Student
# Create your views here.
def student(request):
    # all_data = Student.objects.all()[0] 
    # all_data = Student.objects.all()[:2]     # for support slicing
    # all_data = Student.objects.all()[-1]    # not support in query negetive indexing
    # all_data = Student.objects.all().reverse()
    # all_data = Student.objects.order_by('stu_name')
    # all_data = Student.objects.order_by('-stu_name')        # in reverse order
    all_data = Student.objects.filter(stu_name='Him')       # return empty if empty
    all_data = Student.objects.filter(stu_name='Himanshu')   # return particular user details  only  
    all_data = Student.objects.filter(stu_name='Himanshu', stu_email='himanshu@gmail.com')   # return ...
    all_data = Student.objects.exclude(stu_name = 'Himanshu')  
    # all_data = Student.objects.get(stu_name = 'Himanshu')     # error most time
    all_data = Student.objects.last() 
    # all_data = Student.objects.create(stu_name='Rohit', stu_email='rohit@gmail.com', stu_contact=323243211, stu_city='Satna')       # insert data into database
    data = Student.objects.last()
    # data.delete()          # it delete first data
    data.update(stu_name='Neetu', stu_email='n@gmail.com')
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())
    