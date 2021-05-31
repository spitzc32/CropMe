from app.core.models import BaseModel

from django.db import models
from django.utils.text import slugify


class Crop(BaseModel):
	"""
	Crop model is for the recommended crops that can be planted for a timespan
	this holds the information about crops that may be palntable during the
	forcasted season.
	
	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.

	"""
	name = models.CharField(max_length=45)
	scientific_name = models.CharField(max_length=100)
	image_url = models.CharField(max_length=200)
	family_common_name = models.CharField(max_length=100)
	
	days_to_harvest = models.IntegerField(default=1)
	ph_maximum = models.IntegerField(default=0)
	ph_minimum = models.IntegerField(default=0)
	atmospheric_humidity =  models.IntegerField(default=0)
	soil_humidity = models.FloatField(default=0)

	minimum_precipitation = models.IntegerField(default=0)
	maximum_precipitation = models.IntegerField(default=0)
	
	minimum_temperature = models.FloatField(default=0)
	maximum_temperature = models.FloatField(default=0)
	ave_temperature = models.FloatField(default=0)

	def __str__(self):
		return '{}'.format(self.name) or '{}'.format(self.bot_name)

	@property
	def slug(self):
		return slugify(self.name)	


class CropGrowth(BaseModel):
	"""
	CropGrowth is for the array list of growth_months where a certain crop
	is flourishing at. This is an extension to the model of Crop.

	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.

	"""
	growth_month = models.CharField(max_length=10)
	crop = models.ForeignKey(to=Crop, on_delete=models.CASCADE)

	def __str__(self):
		return '{} - {}'.format(self.growth_month, self.crop.name)


class CropFruit(BaseModel):
	"""
	CropFruit is for the array list of growth_months where a certain crop
	is best condition to bear fruit. This is an extension to the model of Crop.

	Inherited
	---------
		core.Basemodel : class obj
			Contains the basic information of when this object was created etc.
			It also helps deal with deletion records by setting is_active to 
			False.
	
	"""
	fruit_months = models.CharField(max_length=10)
	crop = models.ForeignKey(to=Crop, on_delete=models.CASCADE)

	def __str__(self):
		return '{} - {}'.format(self.fruit_months, self.crop.name)
