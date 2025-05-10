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

# Dashboard
def dashboard(request, pk):
    student = Students.objects.get(id=pk)
    return render(request, 'profile.html', {'userdata': get_user_dict(student.id), 'show_profile': True
})

# Login logic
def logindata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Students.objects.filter(stuemail=email).first()

        if user and password == user.stupass:
            return redirect('profile1', pk=user.id)
        else:
            msg = "Invalid email or password"
            return render(request, 'login.html', {'msg': msg, 'email': email})
    return render(request, 'login.html')


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
# about1
def about1(request, pk):
    return render(request, 'about.html', {'userdata': get_user_dict(pk)})
# service1
def service1(request, pk):
    return render(request, 'service.html', {'userdata': get_user_dict(pk)})
# registration1
def registration1(request, pk):
    return render(request, 'registration.html', {'userdata': get_user_dict(pk)})
# admins1
def admins1(request, pk):
    users = Students.objects.all()
    return render(request, 'admins.html', {'userdata': get_user_dict(pk), 'users': users})

# --------------------- BOOK VIEWS -------------------------

def profile(request):
    return render(request, 'profile.html')

# --------------------- STUDENT BOOK VIEWS -------------------------
def profile1(request, pk):
    user = Students.objects.get(id=pk)
    return render(request, 'profile.html', {'userdata': user, 'show_profile': False
})

def first1(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.all()[:5]
    print(data)
    return render(request, 'profile.html', {'userdata': user, 'data': data})

# or with this way but image not show   : -------------------------------
# def last1(request, pk):
#     return render(request, 'profile.html', {'userdata': get_user_dict(pk), 'data': Book.objects.order_by('-id')[:5]})

def last1(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('-id')[:5]     # Last 5 books in descending order
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def all1(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.all()       # all books
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def asc1(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('student_name')       # in ascending order by name
    return render(request, 'profile.html', {'userdata': user, 'data': data})

def desc1(request, pk):
    user = Students.objects.get(id=pk)
    data = Book.objects.order_by('-student_name')       # in descending order by name
    return render(request, 'profile.html', {'userdata': user, 'data': data}) 