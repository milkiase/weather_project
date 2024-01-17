# weather_app/models.py
from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
