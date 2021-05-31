from app.accounts.models import Account
from app.core.models import BaseModel
from app.crops.models import Crop, CropGrowth, CropFruit
from app.weather.models import WeatherHistory, WeatherForcast

from django.db import models
from django.utils.text import slugify


class UserCropFavorite(BaseModel):
	"""
	UserCropFavorite model is for the retrieved agro weather that is used as
	a dataset to predict what we insert into our WeatherForcast model.
	
	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.

	"""
	crop = models.ForeignKey(to=Crop, on_delete=models.CASCADE)
	crop_growth = models.ForeignKey(to=CropGrowth, on_delete=models.CASCADE)
	crop_fruit = models.ForeignKey(to=CropFruit, on_delete=models.CASCADE)
	user = models.ForeignKey(to=Account, on_delete=models.CASCADE)


class UserCropState(UserCropFavorite):
	"""
	UserCropState model is for the retrieved agro weather that is used as
	a dataset to predict what we insert into our WeatherForcast model.
	
	Inherited
	---------
		.UserCropFavorite : class obj
			Contains the basic information of the crop data a user needs.

	"""
	STATE_CHOICES = (
        ('Seed', 'Seed'),
        ('Planting', 'Planting'),
        ('Harvesting', 'Harvesting'),
        ('Withered', 'Withered'),
    )
	state = models.CharField(max_length=300, choices = STATE_CHOICES)

class UserWeatherHistory(WeatherHistory):
	"""
	WeatherHistory model is for the retrieved agro weather that is used as
	a dataset to predict what we insert into our WeatherForcast model.
	
	Inherited
	---------
		weather.WeatherHistory : class obj
			Contains the basic information of the WeatherHistory we need

	"""
	user = models.ForeignKey(to=Account, on_delete=models.CASCADE)



class UserWeatherForcast(WeatherForcast):
	"""
	UserWeatherForcast model is for the predicted agro weather personalized 
	that is used by our recommendation system following the FAO guidelines.
	
	Inherited
	---------
		weather.WeatherForcast : class obj
			Contains the basic information of the predicted value for
			Weather Forcast

	"""
	user = models.ForeignKey(to=Account, on_delete=models.CASCADE)
