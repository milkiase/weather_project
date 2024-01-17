# weather_app/utils.py
import requests
from django.contrib.auth.models import User
from .models import City

api_key = '11791edf82232148a9ce38dd62cd0dea'

# def get_weather_data(city_name):
#     # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
#     api_key = '11791edf82232148a9ce38dd62cd0dea'
#     url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
#     try:
#         response = requests.get(url)
#         data = response.json()
#         temperature = round((data['main']['temp'] - 273.15), 2)
#         description = data['weather'][0]['description']

#         if not City.objects.filter(name__iexact=city_name).exists():
#             user = User.objects.all()[0]
#             city = City(name=city_name, user=user)
#             city.save()
#         return f'Temperature in {city_name}: {temperature}°C, {description}'
#     except Exception as e:
#         return f'Error fetching data for {city_name}: {e}'

def get_weather_data(city_name, user=None):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        weather_data = {
            'temperature': round((data['main']['temp'] - 273.15), 2),
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'pressure': data['main']['pressure'],
        }
        
        if user:
            if not City.objects.filter(name__iexact=city_name).exists():
                city = City(name=city_name, user=user)
                city.save()
        
        return weather_data
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
    

def get_weather_forecast(city_name):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        forecasts = data['list']
        
        forecast_list = []
        for forecast in forecasts:
            forecast_data = {
                'date': forecast['dt_txt'],
                'temperature':  round((forecast['main']['temp'] - 273.15), 2),
                'humidity': forecast['main']['humidity'],
                'description': forecast['weather'][0]['description'],
            }
            forecast_list.append(forecast_data)
        
        return forecast_list
    
    except Exception as e:
        print(f"Error fetching weather forecast: {e}")
        return []