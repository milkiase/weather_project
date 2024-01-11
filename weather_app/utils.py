# weather_app/utils.py
import requests
from .models import City

def get_weather_data(city_name):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '11791edf82232148a9ce38dd62cd0dea'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    try:
        response = requests.get(url)
        data = response.json()
        temperature = round((data['main']['temp'] - 273.15), 2)
        description = data['weather'][0]['description']
        city = City(name=city_name)
        city.save()
        return f'Temperature in {city_name}: {temperature}°C, {description}'
    except Exception as e:
        return f'Error fetching data for {city_name}: {e}'
