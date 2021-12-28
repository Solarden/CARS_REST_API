import urllib.request
import json

from django.db.models import Avg

from cars_api import models
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def validate(self, values):
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{values["make"]}?format=json'
        response = urllib.request.urlopen(url)
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(response.read().decode(encoding))
        if data['Count'] == 0:
            raise serializers.ValidationError('Car does not exist!')
        else:
            values["make"] = values["make"].lower().title()
            values['model'] = values['model'].lower().title()
            for i in range(0, len(data['Results'])):
                if data['Results'][i]['Model_Name'] == values['model']:
                    return values
            else:
                raise serializers.ValidationError("Car does not exist!")

    def get_id(self, object):
        return object.id

    def get_avg_rating(self, object):
        return models.CarRate.objects.filter(car_id=object.pk).values('rating').aggregate(Avg('rating'))['rating__avg']


class CarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarRate
        fields = ['car_id', 'rating']


class PopularCarsSerializer(serializers.ModelSerializer):
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = models.Car
        fields = ['id', 'make', 'model', 'rates_number']

    def get_rates_number(self, object):
        return models.CarRate.objects.filter(car_id=object.pk).count()
