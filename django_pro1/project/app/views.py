from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def admins(request):
    return render(request, 'admins.html')
def about(request):
    return render(request, 'about.html')
def login(request):
    return render(request, 'login.html')
def registration(request):
    return render(request, 'registration.html')
def service(request):
    return render(request, 'service.html')
def user(request):
    return render(request, 'user.html')


