import logging
from django.db import transaction

from .models import WeatherHistory, WeatherForcast


log = logging.getLogger('default')


def create_weather_hist_record(items):
    transaction.set_autocommit(False)
    try:
        WeatherHistory.objects.bulk_create([
            WeatherHistory(
                latitude=item['lat'],
                longitude=item['lon'],
                date=item['data'][0]['valid_date'],
                bulk_soil_density=item['data'][0]['bulk_soil_density'],
                surface_pressure=item['data'][0]['pres_avg'],
                minimum_temperature=item['data'][0]['skin_temp_min'],
                maximum_temperature =item['data'][0]['skin_temp_max'],
                precipitation=item['data'][0]['precip'],
                atmospheric_humidity=item['data'][0]['specific_humidity'],
                evapotranspiration=item['data'][0]['evapotranspiration'],
                soil_mositure_0_10=item['data'][0]['soilm_0_10cm'],
                soil_mositure_10_40=item['data'][0]['soilm_10_40cm'],
                soil_mositure_40_100=item['data'][0]['soilm_40_100cm'],
                soil_mositure_100_200=item['data'][0]['soilm_100_200cm'],
                soil_temp_0_10=item['data'][0]['soilt_0_10cm'],
                soil_temp_10_40=item['data'][0]['soilt_10_40cm'],
                soil_temp_40_100=item['data'][0]['soilt_0_10cm'],
                soil_temp_100_200=item['data'][0]['soilt_10_40cm'],
				
            ) for item in items
	])
    except Exception:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
        distinct_attributes = WeatherHistory.objects.distinct(
            'date'
        ).order_by(
            'date', 'id'
        ).values('id')
        duplicate_attributes = WeatherHistory.objects.exclude(
            id__in=distinct_attributes
        )
        duplicate_attributes.delete()


def create_weather_fort_record(items):
    transaction.set_autocommit(False)
    try:
        WeatherHistory.objects.bulk_create([
            WeatherHistory(
                latitude=item['latitude'],
                longitude=item['longitude'],
                date=item['data'][0]['date'],
                minimum_temperature=item['minimum_temperature'],
                maximum_temperature =item['maximum_temperature'],
                precipitation=item['precipitation'],
                atmospheric_humidity=item['atmospheric_humidity'],
            ) for item in items
        ])
    except Exception:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
        distinct_attributes = WeatherHistory.objects.distinct(
           'date'
        ).order_by(
           'date', 'id'
        ).values('id')
        duplicate_attributes = WeatherHistory.objects.exclude(
           id__in=distinct_attributes
        )
        duplicate_attributes.delete()
