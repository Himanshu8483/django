from django.shortcuts import render, redirect
from .models import Students

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

def login_view(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == 'admin@gmail.com' and password == 'admin@123':
            request.session['user'] = 'admin'
            return redirect('admin_dashboard')

        elif email == 'student@gmail.com' and password == 'student@123':
            request.session['user'] = 'student'
            return redirect('student_dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def admin_dashboard(request):
    if request.session.get('user') != 'admin':
        return redirect('login')
    return render(request, 'admin_dashboard.html')


def student_dashboard(request):
    if request.session.get('user') != 'student':
        return redirect('login')
    return render(request, 'student_dashboard.html')


def logout_view(request):
    request.session.flush()
    return redirect('login')


# Registration logic
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        subscribe = request.POST.getlist('subscribe')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profilepic = request.FILES.get('profile-pic')
        resume = request.FILES.get('resume')

        if Students.objects.filter(stuemail=email).exists():
            return render(request, 'registration.html', {'error': "Email Already Exists"})

        if password != cpassword:
            return render(request, 'registration.html', {'error': "Check Password And Confirm Password again"})

        Students.objects.create(
            stuname=username,
            stuemail=email,
            studetails=detail,
            stuphone=phone,
            studob=dob,
            stuedu=subscribe,
            stugender=gender,
            stuimage=profilepic,
            sturesume=resume,
            stupass=password
        )
        return render(request, 'login.html', {'error': "Registration Successful"})

    return render(request, 'registration.html')

# Utility function
def get_user_dict(pk):
    user = Students.objects.get(id=pk)
    return {
        "id": user.id,
        "name": user.stuname,
        "email": user.stuemail,
        "des": user.studetails,
        "phone": user.stuphone,
        "dob": user.studob,
        "sub": user.stuedu,
        "gender": user.stugender,
        "image": user.stuimage,
        "resume": user.sturesume,
        "pass": user.stupass,
    }