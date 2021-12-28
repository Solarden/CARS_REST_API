from rest_framework import generics, status, viewsets
from cars_api import models, serializers
from django.db import IntegrityError
from rest_framework.response import Response


class CarsListCreateView(generics.ListCreateAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super(generics.ListCreateAPIView, self).create(request, *args, **kwargs)
        except IntegrityError:
            content = {'error': 'Car model already exist in database!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class CarsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer


#     TODO DELETE /cars/ does not exist


class RateCarsCreateView(generics.CreateAPIView):
    queryset = models.CarRate.objects.all()
    serializer_class = serializers.CarRateSerializer


class PopularCarsListView(generics.ListAPIView):
    queryset = models.Car.objects.all()
    serializer_class = serializers.PopularCarsSerializer
