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

def admins1(request, pk):
    users = Students.objects.all()
    return render(request, 'admins.html', {'userdata': get_user_dict(pk), 'users': users})

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
        if request.session.get('user') != 'student':
            return redirect('login')
        return render(request, 'stuallquery.html', {'userdata': user, 'success': success_msg})

    return render(request, 'newquery.html', {'userdata': user})


def stuallquery(request):
    queries = StuQuery.objects.all().order_by('-created_at')
    return render(request, 'stuallquery.html', {'queries': queries})
