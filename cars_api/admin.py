from django.contrib import admin

# Register your models here.
from cars_api.models import Car, CarRate

admin.site.register(Car)
admin.site.register(CarRate)
