from random import randint

import pytest
from rest_framework.test import APIClient
from cars_api import models


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


@pytest.fixture(autouse=True)
def set_up_car():
    return models.Car.objects.create(make='Ford', model='Focus')


@pytest.fixture(autouse=True)
def set_up_cars():
    models.Car.objects.create(make='Honda', model='Accord')
    models.Car.objects.create(make='Honda', model='Civic')


@pytest.fixture(autouse=True)
def set_up_car_rate(set_up_car):
    return models.CarRate.objects.create(car_id=set_up_car, rating=randint(1, 5))
