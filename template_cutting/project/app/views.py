from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'landing.html')

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def services(request):
    return render(request, 'services.html')
def registration(request):
    return render(request, 'registration.html')
def login(request): 
    return render(request, 'login.html')