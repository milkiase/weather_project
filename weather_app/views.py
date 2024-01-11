# weather_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import City
from .utils import get_weather_data

def index(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'weather_app/index.html', context)

def add_city(request):
    if request.method == 'POST':
        city_name = request.POST['city_name']
        get_weather_data(city_name)
    return HttpResponseRedirect('/')

def city_detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    weather_details = get_weather_data(city.name)
    context = {'city': city, 'weather_details': weather_details}
    return render(request, 'weather_app/city_detail.html', context)
