import numpy as np
import pandas as pd

from .api_operations import *
from app.weather.utils import (
	create_weather_hist_record,
	create_weather_fort_record,
)

URL = ""