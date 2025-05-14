from django.shortcuts import render

# Create your views here.
def set(request):
    data = render(request, 'app/set.html')
    data.set_cookie('name', 'Himanshu')
    data.set_cookie('age', '23')
    data.set_cookie('city', 'Rewa')
    
    return data

def get(request):
    data = render(request, 'app/get.html')
def delete(request):
    data = render(request, 'app/delete.html')
    