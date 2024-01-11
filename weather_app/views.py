# weather_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from .utils import get_weather_data

def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'weather_app/index.html', context)

def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city_name'].strip()
        
        # Check if the city already exists in the database
        if not City.objects.filter(name__iexact=city_name).exists():
            get_weather_data(city_name)
        
    return HttpResponseRedirect(reverse('index'))

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    weather_details = get_weather_data(city.name)
    context = {'city': city, 'weather_details': weather_details}
    return render(request, 'weather_app/city_detail.html', context)
