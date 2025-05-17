from django.shortcuts import render, redirect
from .models import Students, StuQuery   

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def login(request):
    return render(request, 'login.html')

def registration(request):
    return render(request, 'registration.html')

# Utility function
def get_user_dict(pk):
    user = Students.objects.get(id=pk)
    return {
        "id": user.id,
        "stuname": user.stuname,
        "stuemail": user.stuemail,
        "studetail": user.studetail,
        "stuphone": user.stuphone,
        "studob": user.studob,
        "stuedu": user.stuedu,
        "stugender": user.stugender,
        "stuimage": user.stuimage,
        "sturesume": user.sturesume,
        "stupass": user.stupass,
    }
    
def home1(request, pk):
    return render(request, 'home.html', {'userdata': get_user_dict(pk)})

def about1(request, pk):
    return render(request, 'about.html', {'userdata': get_user_dict(pk)})

def service1(request, pk):
    return render(request, 'service.html', {'userdata': get_user_dict(pk)})

def registration1(request, pk):
    return render(request, 'registration.html', {'userdata': get_user_dict(pk)})

def student_dashboard1(request, pk):
    user = Students.objects.get(id=pk)
    return render(request, 'student_dashboard.html', {'userdata': user})
    
def admin_dashboard1(request, pk):
    user = Students.objects.get(id=pk)
    if request.session.get('user') != 'admin':
        return redirect('login')
    users = Students.objects.all()
    return render(request, 'admin_dashboard.html', { 'users': users, 'user':user})    

def admin_dashboard(request):
    if request.session.get('user') != 'admin':
        return redirect('login')
    users = Students.objects.all()
    return render(request, 'admin_dashboard.html', { 'users': users})

def student_dashboard(request):
    if request.session.get('user') != 'student':
        return redirect('login')
    return render(request, 'student_dashboard.html')


def logout(request):
    request.session.flush()
    return redirect('login')

def logindata(request):
    if request.method == 'POST':
        email = request.POST.get('stuemail')
        password = request.POST.get('stupass')

        # Admin login
        if email == 'admin@gmail.com' and password == 'admin@123':
            request.session['user'] = 'admin'
            return redirect('admin_dashboard')

        # Student login (from database)
        student = Students.objects.filter(stuemail=email).first()
        if student and password == student.stupass:
            request.session['user'] = 'student'
            request.session['student_id'] = student.id  
            return redirect('student_dashboard1', pk=student.id)

        # Invalid login
        msg = "Invalid email or password"
        return render(request, 'login.html', {'msg': msg, 'stuemail': email})

    return render(request, 'login.html')


# Registration logic
def register(request):
    if request.method == 'POST':
        stuname = request.POST.get('stuname')
        stuemail = request.POST.get('stuemail')
        studetail = request.POST.get('studetail')
        stuphone = request.POST.get('stuphone')
        studob = request.POST.get('studob')
        stuedu = request.POST.getlist('stuedu')
        stugender = request.POST.get('stugender')
        stupass = request.POST.get('stupass')
        cpass = request.POST.get('cpass')
        stuimage = request.FILES.get('stuimage')
        sturesume = request.FILES.get('sturesume')

        if Students.objects.filter(stuemail=stuemail).exists():
            return render(request, 'registration.html', {'error': "Email Already Exists"})

        if cpass != cpass:
            return render(request, 'registration.html', {'error': "Check Password And Confirm Password again"})

        Students.objects.create(
            stuname=stuname,
            stuemail=stuemail,
            studetail=studetail,
            stuphone=stuphone,
            studob=studob,
            stuedu=stuedu,
            stugender=stugender,
            stuimage=stuimage,
            sturesume=sturesume,
            stupass=stupass
        )
        # return render(request, 'admin_dash.html', {'error': "Registration Successful"})
        return redirect('admin_dashboard')
    

    return render(request, 'registration.html')


def allquery(request):
    queries = StuQuery.objects.all().order_by('-created_at')
    return render(request, 'allquery.html', {'queries': queries})


def queryres(request, pk):
    query = StuQuery.objects.get(id=pk)
    if request.method == 'POST':
        response = request.POST.get('response')
        query.response = response
        query.save()
        return redirect('allquery')
    return render(request, 'queryres.html', {'query': query})


def newquery(request, pk):
    user = Students.objects.get(id=pk)
    if request.session.get('user') != 'student':
        return redirect('login')
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')

        StuQuery.objects.create(
            stuname=user.stuname,
            stuemail=user.stuemail,
            title=title,
            message=message
        )
        success_msg = "Query submitted successfully!"

        return redirect('stuallquery', pk=user.id)

    return render(request, 'newquery.html', {'userdata': user})

def stuallquery(request, pk):
    user = Students.objects.get(id=pk)
    # Filter queries only for this user
    queries = StuQuery.objects.filter(stuname=user.stuname, stuemail=user.stuemail).order_by('-created_at')
    return render(request, 'stuallquery.html', {'queries': queries, 'userdata': user})


def edituser(request, pk):
    students = Students.objects.all()
    student =  Students.objects.get(id=pk)
    context = {
        'userdata': student,
        'users': students,
        'showform': True, 

    }
    return render(request, 'admin_dashboard.html', context)
def edituserdata(request, pk):
    if request.method == "POST":
        student = Students.objects.get(id=pk)
        
        student.stuname = request.POST.get('stuname')
        student.stuemail = request.POST.get('stuemail')
        student.stuphone = request.POST.get('stuphone')
        student.studetail = request.POST.get('studetail')
        
        if request.POST.get('studob'):
            student.studob = request.POST.get('studob')

        # if request.POST.getlist('stuedu'):
        #     student.stuedu = ','.join(request.POST.getlist('stuedu'))

        if request.POST.getlist('stuedu'):
            student.stuedu = request.POST.getlist('stuedu')

        if request.POST.get('stugender'):
            student.stugender = request.POST.get('stugender')

        if 'stuimage' in request.FILES:
            student.stuimage = request.FILES['stuimage']

        if 'sturesume' in request.FILES:
            student.sturesume = request.FILES['sturesume']

        if request.POST.get('stupass'):
            student.stupass = request.POST.get('stupass')

        student.save()

        users = Students.objects.all()
        return render(request, 'admin_dashboard.html', {
            'userdata': student,
            'users': users,
            'show_profile': True
        })

def deleteuser(request, pk):
    student = Students.objects.get(id=pk)
    student.delete()
    return redirect('admin_dashboard')


def editquery(request, pk1, pk):
    student = Students.objects.get(id=pk1)
    query = StuQuery.objects.get(id=pk)
    queries = StuQuery.objects.all()
    context = {
        'userdata': get_user_dict(student.id),
        'editdata': query,
        'data': queries,
        'showform': True,
    }
    return render(request, 'stuallquery.html', context)


def edituserquery(request, pk1, pk):
    if request.method == "POST":
        query = StuQuery.objects.get(id=pk)
        query.title = request.POST.get('title')
        query.message = request.POST.get('message')
        query.save()
        return redirect('stuallquery', pk=pk1)
    return redirect('stuallquery', pk=pk1)


def deletequery(request, pk1, pk):
    query = StuQuery.objects.get(id=pk)
    query.delete()
    return redirect('stuallquery', pk=pk1)



def first1(request):
    queries = StuQuery.objects.all()[:5]
    print(queries)
    return render(request, 'allquery.html', {'queries': queries})

def last1(request):
    queries = StuQuery.objects.order_by('-id')[:5]     # Last 5 Querys in descending order
    return render(request, 'allquery.html', {'queries': queries})

def asc1(request):
    queries = StuQuery.objects.order_by('stuname')       # in ascending order by name
    return render(request, 'allquery.html', {'queries': queries})

def desc1(request):
    queries = StuQuery.objects.order_by('-stuname')       # in descending order by name
    return render(request, 'allquery.html', {'queries': queries}) 

