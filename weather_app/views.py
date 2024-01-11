# weather_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests
from django.http import JsonResponse
from django.db.models import Q
from .models import City
from .utils import get_weather_data

def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'weather_app/index.html', context)

def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city_name'].strip()
        
        # Check if the city already exists in the database (case-insensitive)
        if not City.objects.filter(name__iexact=city_name).exists():
            get_weather_data(city_name)
        
    return HttpResponseRedirect(reverse('index'))

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    weather_details = get_weather_data(city.name)
    context = {'city': city, 'weather_details': weather_details}
    return render(request, 'weather_app/city_detail.html', context)

def city_autocomplete(request):
    term = request.GET.get('term', None)
    if term:
        api_key = '11791edf82232148a9ce38dd62cd0dea'
        url = f'http://api.openweathermap.org/geo/1.0/direct?q={term}&limit=5&appid={api_key}'
        
        try:
            response = requests.get(url)
            data = response.json()
            suggestions = [city['name'] for city in data]
            return JsonResponse(suggestions, safe=False)
        except Exception as e:
            print(f"Error fetching suggestions: {e}")

    return JsonResponse([], safe=False)