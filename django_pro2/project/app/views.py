from django.shortcuts import render, redirect
from .models import Users, UserQuery   
from django.core.paginator import Paginator

from django.db.models import Q
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
    user = Users.objects.get(id=pk)
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

def user_dashboard1(request, pk):
    user = Users.objects.get(id=pk)
    return render(request, 'user_dashboard.html', {'userdata': user})
    
def admin_dashboard1(request, pk):
    user = Users.objects.get(id=pk)
    if request.session.get('user') != 'admin':
        return redirect('login')
    users = Users.objects.all()
    return render(request, 'admin_dashboard.html', { 'users': users, 'user':user})    

def admin_dashboard(request):
    if request.session.get('user') != 'admin':
        return redirect('login')
    users = Users.objects.all()
    return render(request, 'admin_dashboard.html', { 'users': users})

def user_dashboard(request):
    if request.session.get('user') != 'student':
        return redirect('login')
    return render(request, 'user_dashboard.html')


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
        student = Users.objects.filter(stuemail=email).first()
        if student and password == student.stupass:
            request.session['user'] = 'student'
            request.session['student_id'] = student.id  
            return redirect('user_dashboard1', pk=student.id)

        # Invalid login
        msg = "Invalid email or password"
        return render(request, 'login.html', {'msg': msg, 'stuemail': email})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        stuname = request.POST.get('stuname')
        stuemail = request.POST.get('stuemail')
        studetail = request.POST.get('studetail')
        stuphone = request.POST.get('stuphone')
        studob = request.POST.get('studob')
        stuedu = request.POST.getlist('stuedu')
        stuedu = ", ".join(stuedu)  # convert list to comma-separated string
        
        stugender = request.POST.get('stugender')
        stupass = request.POST.get('stupass')
        cpass = request.POST.get('cpass')
        stuimage = request.FILES.get('stuimage')
        sturesume = request.FILES.get('sturesume')

        # Name validation: allow only letters and spaces
        for ch in stuname:
            if not (ch.isalpha() or ch == ' '):
                return render(request, 'registration.html', {'error': "Name can only contain letters and spaces."})

        # Phone validation
        if len(stuphone) != 10 or not stuphone.isdigit():
            return render(request, 'registration.html', {'error': "Phone number must be exactly 10 digits."})

        if stuphone[0] == '0':
            return render(request, 'registration.html', {'error': "Phone number cannot start with 0."})

        
        if stuphone == stuphone[0] * 10:
            return render(request, 'registration.html', {'error': "Phone number cannot be all digits same."})

        if '@gmail.com' not in stuemail:
            return render(request, 'registration.html', {'error': "Email must include @gmail.com"})

        if Users.objects.filter(stuemail=stuemail).exists():
            return render(request, 'registration.html', {'error': "Email Already Exists"})

        if stupass != cpass:
            return render(request, 'registration.html', {'error': "Password and Confirm Password do not match."})

        if len(stupass) < 8:
            return render(request, 'registration.html', {'error': "Password must be at least 8 characters long."})

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        special_chars = "!@#$%^&*()-_+=[]{}|\\;:'\",.<>/?`~"

        for ch in stupass:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_chars:
                has_special = True

        if not (has_upper and has_lower and has_digit and has_special):
            return render(request, 'registration.html', {'error': "Password must include uppercase, lowercase, digit, and special character."})

        # All validations passed — create user
        Users.objects.create(
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

        return redirect('admin_dashboard')

    return render(request, 'registration.html')

# def allquery(request):
#     queries = UserQuery.objects.all().order_by('-created_at')
#     return render(request, 'allquery.html', {'queries': queries})

def allquery(request):
    queries = UserQuery.objects.all().order_by('-created_at')
    paginator = Paginator(queries, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'allquery.html', {'page_obj': page_obj, 'queries': page_obj})

def queryres(request, pk):
    query = UserQuery.objects.get(id=pk)
    if request.method == 'POST':
        response = request.POST.get('response')
        query.response = response
        query.save()
        return redirect('allquery')
    return render(request, 'queryres.html', {'query': query})


def newquery(request, pk):
    user = Users.objects.get(id=pk)
    if request.session.get('user') != 'student':
        return redirect('login')
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')

        UserQuery.objects.create(
            stuname=user.stuname,
            stuemail=user.stuemail,
            title=title,
            message=message
        )
        success_msg = "Query submitted successfully!"

        return redirect('userallquery', pk=user.id)

    return render(request, 'newquery.html', {'userdata': user})

def userallquery(request, pk):
    user = Users.objects.get(id=pk)
    # Filter queries only for this user
    queries = UserQuery.objects.filter(stuname=user.stuname, stuemail=user.stuemail).order_by('-created_at')
    return render(request, 'userallquery.html', {'queries': queries, 'userdata': user})


def edituser(request, pk):
    users = Users.objects.all()
    student =  Users.objects.get(id=pk)
    context = {
        'userdata': student,
        'users': users,
        'showform': True, 

    }
    return render(request, 'admin_dashboard.html', context)
def edituserdata(request, pk):
    student = Users.objects.get(id=pk)
    users = Users.objects.all()

    if request.method == "POST":
        stuname = request.POST.get('stuname')
        stuemail = request.POST.get('stuemail')
        stuphone = request.POST.get('stuphone')
        studetail = request.POST.get('studetail')
        studob = request.POST.get('studob')
        stuedu = request.POST.getlist('stuedu')
        stuedu = ", ".join(stuedu)  # convert list to comma-separated string
        stugender = request.POST.get('stugender')
        stuimage = request.FILES.get('stuimage')
        sturesume = request.FILES.get('sturesume')
        stupass = request.POST.get('stupass')

        # --- Validation ---

        # Name validation
        if stuname:
            for ch in stuname:
                if not (ch.isalpha() or ch == ' '):
                    return render(request, 'admin_dashboard.html', {
                        'error': "Name can only contain letters and spaces.",
                        'userdata': student,
                        'showform': True,
                        'users': users
                    })

        # Phone validation
        if stuphone:
            if len(stuphone) != 10 or not stuphone.isdigit():
                return render(request, 'admin_dashboard.html', {
                    'error': "Phone number must be exactly 10 digits.",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })
            if stuphone[0] == '0':
                return render(request, 'admin_dashboard.html', {
                    'error': "Phone number cannot start with 0.",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })
            if stuphone == stuphone[0] * 10:
                return render(request, 'admin_dashboard.html', {
                    'error': "Phone number cannot be all digits same.",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })

        # Email validation
        if stuemail:
            if '@gmail.com' not in stuemail:
                return render(request, 'admin_dashboard.html', {
                    'error': "Email must include @gmail.com",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })
            if Users.objects.exclude(id=pk).filter(stuemail=stuemail).exists():
                return render(request, 'admin_dashboard.html', {
                    'error': "Email Already Exists",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })

        if stupass:
            if len(stupass) < 8:
                return render(request, 'admin_dashboard.html', {
                    'error': "Password must be at least 8 characters long.",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })
            has_upper = False
            has_lower = False
            has_digit = False
            has_special = False
            special_chars = "!@#$%^&*()-_+=[]{}|\\;:'\",.<>/?`~"

            for ch in stupass:
                if ch.isupper():
                    has_upper = True
                elif ch.islower():
                    has_lower = True
                elif ch.isdigit():
                    has_digit = True
                elif ch in special_chars:
                    has_special = True

            if not (has_upper and has_lower and has_digit and has_special):
                return render(request, 'admin_dashboard.html', {
                    'error': "Password must include uppercase, lowercase, digit, and special character.",
                    'userdata': student,
                    'showform': True,
                    'users': users
                })

        student.stuname = stuname
        student.stuemail = stuemail
        student.stuphone = stuphone
        student.studetail = studetail

        if studob:
            student.studob = studob

        if stuedu:
            student.stuedu = stuedu

        if stugender:
            student.stugender = stugender

        if stuimage:
            student.stuimage = stuimage

        if sturesume:
            student.sturesume = sturesume

        if stupass:
            student.stupass = stupass

        student.save()

        users = Users.objects.all()
        return render(request, 'admin_dashboard.html', {
            'userdata': student,
            'users': users,
        })

    return render(request, 'admin_dashboard.html', {'userdata': student})

def deleteuser(request, pk):
    student = Users.objects.get(id=pk)
    student.delete()
    return redirect('admin_dashboard')


def editquery(request, pk1, pk):
    student = Users.objects.get(id=pk1)
    query = UserQuery.objects.get(id=pk)
    queries = UserQuery.objects.all()
    context = {
        'userdata': get_user_dict(student.id),
        'editdata': query,
        'data': queries,
        'showform': True,
    }
    return render(request, 'userallquery.html', context)


def edituserquery(request, pk1, pk):
    if request.method == "POST":
        query = UserQuery.objects.get(id=pk)
        query.title = request.POST.get('title')
        query.message = request.POST.get('message')
        query.save()
        return redirect('userallquery', pk=pk1)
    return redirect('userallquery', pk=pk1)


def deletequery(request, pk1, pk):
    query = UserQuery.objects.get(id=pk)
    query.delete()
    return redirect('userallquery', pk=pk1)



def first1(request):
    queries = UserQuery.objects.all()[:5]
    print(queries)
    return render(request, 'allquery.html', {'queries': queries})

def last1(request):
    queries = UserQuery.objects.order_by('-id')[:5]     # Last 5 Querys in descending order
    return render(request, 'allquery.html', {'queries': queries})

def asc1(request):
    queries = UserQuery.objects.order_by('stuname')
    paginator = Paginator(queries, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'allquery.html', {'page_obj': page_obj, 'queries': page_obj})

def desc1(request):
    queries = UserQuery.objects.order_by('-stuname')       # in descending order by name
    paginator = Paginator(queries, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'allquery.html', {'page_obj': page_obj, 'queries': page_obj})

# def search(request):
#     query = request.GET.get('q')
#     all_queries = UserQuery.objects.all()  
#     if query:
#         queries = [q for q in all_queries if query.lower() in q.stuname.lower()]
#     else:
#         queries = all_queries
#     return render(request, 'allquery.html', {'queries': queries, 'search_term': query})


# def search(request):
#     pk = request.POST.get('search')
#     all_data = UserQuery.objects.filter(Q(stuname__icontains=pk) | Q(stuemail__icontains=pk))
    
#     return render(request, 'allquery.html', {'data': all_data})

# without pagination 
def search(request):
    pk = request.GET.get('search')
    all_data = UserQuery.objects.filter(Q(stuname__icontains=pk) | Q(stuemail__icontains=pk))
    return render(request, 'allquery.html', {'data': all_data, 'pk': pk})


def searchall(request):
    #  but not search by only fill one field requre to fill all input field 
    if request.method == 'POST':
        stuname=request.POST.get('stuname')
        stuemail=request.POST.get('stuemail')
        title=request.POST.get('title')
        
        all_data = UserQuery.objects.filter(Q(stuname__icontains=stuname) | Q(stuemail__icontains=stuemail) | Q(title__icontains=title))
        return render(request, 'allquery.html', {'data': all_data})
    return render(request, 'allquery.html')

# with pagination 
def search(request):
    pk = request.GET.get('search', '')
    data = UserQuery.objects.filter(Q(stuname__icontains=pk) | Q(stuemail__icontains=pk)) if pk else UserQuery.objects.all()

    paginator = Paginator(data, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'pk': pk,
    }
    return render(request, 'allquery.html', context)


def searchall(request):
    if request.method == 'POST':
        stuname = request.POST.get('stuname', '').strip()
        stuemail = request.POST.get('stuemail', '').strip()
        title = request.POST.get('title', '').strip()

        if stuname or stuemail or title:
            data = UserQuery.objects.filter(
                Q(stuname__icontains=stuname),
                Q(stuemail__icontains=stuemail),
                Q(title__icontains=title)
            )
        else:
            data = []  # return empty list if any field is missing

        return render(request, 'allquery.html', {'queries': data, 'stuname': stuname, 'stuemail': stuemail, 'title': title})

    return render(request, 'allquery.html')
