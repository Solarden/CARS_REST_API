from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.pk}'


RATING = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class CarRate(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField(choices=RATING)
