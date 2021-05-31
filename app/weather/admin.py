from django.contrib import admin
from .models import WeatherHistory, WeatherForcast

admin.site.register(WeatherHistory)
admin.site.register(WeatherForcast)
