from random import randint

import pytest
from rest_framework.test import APIClient
from cars_api import models


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up_car():
    return models.Car.objects.create(make='Ford', model='Focus')


@pytest.fixture
def set_up_cars():
    models.Car.objects.create(make='Honda', model='Accord')
    models.Car.objects.create(make='Honda', model='Civic')


@pytest.fixture
def set_up_car_rate(set_up_car):
    return models.CarRate.objects.create(car_id=set_up_car, rating=randint(1, 5))
