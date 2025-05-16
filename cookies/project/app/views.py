from django.shortcuts import render, redirect

# # Create your views here.
# def set(request):
#     data = render(request, 'app/set.html')
#     data.set_cookie('name', 'Himanshu')
#     data.set_cookie('age', '23', max_age=20*60*60)
#     data.set_cookie('city', 'Rewa', httponly=True, secure=True)
#     return data

# def get(request):
#     # print('getCookies')
#     name = request.COOKIES['name']
#     age = request.COOKIES['age']
#     city = request.COOKIES['city']
#     print(name)
#     data = {'name':name, 'age': age, 'city':city}
    
#     return render(request, 'app/get.html', {'data': data})

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def sett(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
#  In Django, you cannot set cookies without having a response object first.
        response = render(request, 'login.html')
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        response.set_cookie('city', city)
        return response
    return redirect('register')

def gett(request):
    if request.method == 'POST':
        name_input = request.POST.get('name')
        email_input = request.POST.get('email')

        # Use get() to avoid KeyError
        cookie_name = request.COOKIES.get('name')
        cookie_email = request.COOKIES.get('email')

        if name_input == cookie_name and email_input == cookie_email:
            return redirect('dashboard')  # Use redirect for safety
        else:
            return render(request, 'register.html')
    return redirect('register')


def delete(request):
    response = redirect('register')  
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('city')
    return response
