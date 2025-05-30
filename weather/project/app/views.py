from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render

def index(request):
    weather_data = {}
    if request.method == 'POST':
        city = request.POST.get('city')
        # api_key = 'your_api_key_here'  # Get it from OpenWeatherMap
        api_key = '47bb059c96c5ce714b9e043ba017053a'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        print("API response:", data)  # Add this to see what API sends back

        if data.get('cod') == 200:
            weather_data = {
                # 'city': city,
                'city': f"{data['name']}, {data['sys']['country']}",  
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data['error'] = "City not found."

    return render(request, 'index.html', {'weather': weather_data})
