from django.shortcuts import render
from .models import Student, Department
# Create your views here.
def student(request):
    all_data = Student.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())
    
    data = Student.objects.get(stu_name = 'Him')
    print(data.stu_name)
    print(data.stu_email)
    print(data.stu_contact)
    print(data.stu_dep.dep_name)
    print(data.stu_dep.dep_dis)
    print(data.stu_dep.dep_hod)
    
def department(request):
    all_data = Department.objects.all()
    print(all_data)
    print(all_data.values())
    print(all_data.values_list())
    
    data = Department.objects.get(dep_name='Data Analyst')
    print(data.students)        # it return None
    all_student = data.students.all()
    print(all_student)