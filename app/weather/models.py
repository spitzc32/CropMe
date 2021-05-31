from app.core.models import BaseModel

from django.db import models
from django.utils.text import slugify


class WeatherHistory(BaseModel):
	"""
	WeatherHistory model is for the retrieved agro weather that is used as
	a dataset to predict what we insert into our WeatherForcast model.
	
	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.

	"""
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	date = models.DateTimeField(null=True)

	#bulk soil density kg/m^3 and surface pressure mb
	bulk_soil_density = models.FloatField(default=0)
	surface_pressure = models.FloatField(default=0)

	# skin_temp_max and skin_temp_min and precip
	minimum_temperature = models.FloatField(default=0)
	maximum_temperature = models.FloatField(default=0)
	precipitation = models.IntegerField(default=0)
	
	# specific_humidity
	atmospheric_humidity = models.FloatField(default=0)
	evapotranspiration = models.FloatField(default=0)

	# soilm_0_10cm - 200cm (mm)
	soil_mositure_0_10 = models.FloatField(default=0)
	soil_mositure_10_40 = models.FloatField(default=0)
	soil_mositure_40_100 = models.FloatField(default=0)
	soil_mositure_100_200 = models.FloatField(default=0)

	# soilt_0_10cm - 200cm (C)
	soil_temp_0_10 = models.FloatField(default=0)
	soil_temp_10_40 = models.FloatField(default=0)
	soil_temp_40_100 = models.FloatField(default=0)
	soil_temp_100_200 = models.FloatField(default=0)

	def __str__(self):
		return '{}'.format(self.name) or '{}'.format(self.date)


class WeatherForcast(BaseModel):
	"""
	WeatherForcast model is for the predicted agro weather that is used by
	our recommendation system following the FAO guidelines.
	
	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.

	"""
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	date = models.DateTimeField(null=True)

	minimum_temperature = models.FloatField(default=0)
	maximum_temperature = models.FloatField(default=0)
	ave_temperature = models.FloatField(default=0)
	
	atmospheric_humidity = models.FloatField(default=0)
	precipitation = models.IntegerField(default=0)
	