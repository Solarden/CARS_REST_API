import urllib.request
import json

from cars_api import models
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = ['make', 'model']

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
