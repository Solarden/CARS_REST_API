import pytest
from cars_api import models


@pytest.mark.django_db
def test_add_car(client, set_up_cars):
    set_up_count = models.Car.objects.count()
    a = {
        'make': 'Ford',
        'model': 'Focus'
    }
    response = client.post('/cars/', data=a, format='json')
    assert response.status_code == 201
    assert models.Car.objects.count() == set_up_count + 1
    for key, value in a.items():
        assert key in response.data
        assert response.data[key] == value


@pytest.mark.django_db
def test_add_not_existing_car(client):
    a = {
        'make': 'Honda',
        'model': 'Nonexistence'
    }
    response = client.post('/cars/', data=a, format='json')
    assert response.status_code == 400


@pytest.mark.django_db
def test_get_cars_list(client, set_up_cars):
    response = client.get('/cars/', {}, format='json')
    assert response.status_code == 200
    assert models.Car.objects.count() == len(response.data)


@pytest.mark.django_db
def test_get_car_detail(client, set_up_cars):
    car = models.Car.objects.first()
    response = client.get(f'/cars/{car.id}/', {}, format='json')
    assert response.status_code == 200
    for field in ('id', 'make', 'model', 'avg_rating'):
        assert field in response.data


@pytest.mark.django_db
def test_delete_car(client, set_up_cars):
    car = models.Car.objects.first()
    response = client.delete(f'/cars/{car.id}/', {}, format='json')
    assert response.status_code == 204
    car_ids = [car.id for car in models.Car.objects.all()]
    assert car.id not in car_ids


@pytest.mark.django_db
def test_update_car(client, set_up_cars):
    car = models.Car.objects.first()
    response = client.get(f'/cars/{car.id}/', {}, format='json')
    car_data = response.data
    new_model = 'Fit'
    car_data['model'] = new_model
    response = client.patch(f'/cars/{car.id}/', car_data, format='json')
    assert response.status_code == 200
    car_obj = models.Car.objects.get(id=car.id)
    assert car_obj.model == new_model
