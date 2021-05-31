import logging
from django.db import transaction

from .models import Crop, CropGrowth, CropFruit


log = logging.getLogger('default')


def create_crop_record(items):
    transaction.set_autocommit(False)
    try:
        Crop.objects.bulk_create([
            Crop(
                name=item['name'],
                scientific_name=item['scientific_name'],
                image_url=item['image_url'],
                family_common_name=item['family_common_name'],
                days_to_harvest=item['days_to_harvest'],
                ph_maximum=item['ph_maximum'],
                ph_minimum =item['ph_minimum'],
                atmospheric_humidity=item['atmospheric_humidity'],
                minimum_precipitation=item['minimum_precipitation'],
                maximum_precipitation=item['maximum_precipitation'],
                minimum_temperature=item['minimum_temperature'],
                maximum_temperature=item['maximum_temperature'],
                soil_humidity=item['soil_humidity'],
            ) for item in items
        ])
    except Exception:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
        distinct_attributes = Crop.objects.distinct(
           'name'
        ).order_by(
           'name', 'id'
        ).values('id')
        duplicate_attributes = Crop.objects.exclude(
            id__in=distinct_attributes
        )
        duplicate_attributes.delete()


def create_crop_growth_record(name,items):
    crop_list = []
    transaction.set_autocommit(False)
    try:
        for item in items:
            for month in item['growth_month']:
                crop = Crop.objects.get(name=name)
                crop_list.append(
                    CropGrowth(
                        growth_month=month,
                        crop=crop
                    )
                )
            CropGrowth.objects.bulk_create(crop_list)
    except Exception:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)


def create_crop_fruit_record(name,items):
    crop_list = []
    transaction.set_autocommit(False)
    try:
        for item in items:
            for month in item['fruit_months']:
                crop = Crop.objects.get(name=name)
                crop_list.append(
                    CropFruit(
                        growth_month=month,
                        crop=crop
                    )
                )

                CropFruit.objects.bulk_create(crop_list)
    except Exception:
        transaction.rollback()
        raise
    else:
        transaction.commit()
    finally:
        transaction.set_autocommit(True)
