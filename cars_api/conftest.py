import pytest
from rest_framework.test import APIClient
from cars_api import models


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up_cars():
    models.Car.objects.create(make='Honda', model='Accord')
    models.Car.objects.create(make='Honda', model='Civic')
