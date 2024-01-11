# weather_app/urls.py
from django.urls import path
from .views import index, add_city, city_detail

urlpatterns = [
    path('', index, name='index'),
    path('add_city/', add_city, name='add_city'),
    path('city_detail/<int:city_id>/', city_detail, name='city_detail'),
]
