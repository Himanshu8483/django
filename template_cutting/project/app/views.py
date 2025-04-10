from django.shortcuts import render
from django.http import HttpResponse

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

def register(request):
    print(request.method)
    print(request.POST)
    print(request.FILES)
    name = request.POST.get('username')
    email = request.POST.get('email')
    detail = request.POST.get('detail')
    phone = request.POST.get('phone')
    dob = request.POST.get('dob')
    gender = request.POST.get('gender')
    education = request.POST.getlist('subscribe')
    profile_pic = request.FILES.get('profile-pic')      # _ used here because hyphon(-) cannot be used
    resume = request.FILES.get('resume')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    
    print(name, email, detail, phone, dob, gender, education, profile_pic, resume, password, cpassword)
    # return HttpResponse("Form submitted successfully")
