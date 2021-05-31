from django.contrib import admin
from .models import Crop, CropGrowth, CropFruit

admin.site.register(Crop)
admin.site.register(CropGrowth)
admin.site.register(CropFruit)