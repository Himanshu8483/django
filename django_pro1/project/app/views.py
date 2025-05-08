from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Students, Book

# Public Pages
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

def admins(request):
    users = Students.objects.all()
    return render(request, 'admins.html', {'users': users})


# Session-based Dashboard
def dashboard(request, pk):
    if not request.session.get('user_id'):
        return redirect('login')

    student = Students.objects.get(id=pk)
    return render(request, 'dashboard.html', {'userdata': get_user_dict(student.id)})


# Login logic
def logindata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Students.objects.filter(stuemail=email).first()

        if user and password == user.stupass:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.stuname
            return redirect('dashboard', pk=user.id)
        else:
            msg = "Invalid email or password"
            return render(request, 'login.html', {'msg': msg, 'email': email})
    return render(request, 'login.html')


# Logout
def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
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
            return render(request, 'registration.html', {'key': "Email Already Exists"})

        if password != cpassword:
            return render(request, 'registration.html', {'key': "Check Password And Confirm Password again"})

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
        return render(request, 'login.html', {'key': "Registration Successful"})

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

# Home1
def home1(request, pk):
    return render(request, 'home.html', {'userdata': get_user_dict(pk)})

# --------------------- BOOK VIEWS -------------------------

def profile(request):
    return render(request, 'profile.html')


# --------------------- STUDENT BOOK VIEWS -------------------------
def student_profile(request, pk):
    user = Students.objects.get(id=pk)
    return render(request, 'profile.html', {'userdata': user})

def student_books_first(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.all()[:5]
    return render(request, 'profile.html', {'userdata': user, 'data': data})
# def student_books_last(request, pk):
#     return render(request, 'profile.html', {'userdata': get_user_dict(pk), 'data': Book.objects.order_by('-id')[:5]})

# def student_books_all(request, pk):
#     return render(request, 'profile.html', {'userdata': get_user_dict(pk), 'data': Book.objects.all()})

def student_books_last(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('-id')[:5]
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def student_books_all(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.all()
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def student_books_asc(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('student_name')
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def student_books_desc(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('-student_name')
    return render(request, 'profile.html', {'userdata': user, 'data': data})
