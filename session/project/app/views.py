from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
from django.shortcuts import render, redirect

def dashboard(request):
    name = request.session.get('name')
    email = request.session.get('email')
    
    if name and email:
        return render(request, 'dashboard.html', {'name': name, 'email': email})
    else:
        return redirect('login') 

def delete_session(request):
    del request.session['name']
    del request.session['email']

    return redirect('login')

def regdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        request.session['name'] = name
        request.session['email'] = email
        request.session['city'] = city
        return render(request, 'login.html')
    return redirect('register')

def logdata(request):
    if request.method == 'POST':
        namef = request.POST.get('name')
        emailf = request.POST.get('email')

        name = request.session.get('name')
        email = request.session.get('email')

        if name == namef and email == emailf:
            return redirect('dashboard')  
        else:
            return render(request, 'login.html')
    return redirect('login')
