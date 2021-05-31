from django.contrib import admin
from .models import (
	UserCropFavorite, 
	UserCropState,
	UserWeatherHistory,
	UserWeatherForcast,
)

admin.site.register(UserCropFavorite)
admin.site.register(UserCropState)
admin.site.register(UserWeatherHistory)
admin.site.register(UserWeatherForcast)
