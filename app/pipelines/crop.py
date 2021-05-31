import numpy as np
import pandas as pd

from .api_operations import *
from app.crops.utils import (
	create_crop_record,
	create_crop_growth_record,
	create_crop_fruit_record,
)


"""
This pipeline is intended use for doing get request to insert the gathered
data having a new structure inside our database. You can access the api used
in this website, https://trefle.io/

API Key
-------
	see the token below

Description
-----------
This is a scheduled pipeline dedicated to get crop information for our
recommendation system in what crops or plants is good to grow due to
the effects of climate change today.

"""

URL = "https://trefle.io/api/v1/species"
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
	'July', 'August', 'September', 'October', 'November', 'December']
TEMP = [0,'celcius']


CROP_PARAMS = {
	'token': 'UP4HP2iLWODxPPYe5Rm-a8pZ12k0WEgf285ajJthnw8'
	'days_to_harvest': 1, # up till 500 days
	'ph_maximum' : 0, # 0-14
	'ph_minimum' : 0, #0-14
	'atmospheric_humidity': 0, #scale 0-10
	'growth_months': MONTHS,
	'fruit_months':MONTHS,
	'minimum_precipitation': 0, #mm per year
	'maximum_precipitation' : 0, #mm per year
	'minimum_temperature ': TEMP, # object celcius
	'maximum_temperature ': TEMP, # object celcius
	'soil_humidity': 0, # 0(xerophile) to 10 (subaquatic)

}
def pipeline():
	pass



