from rest_framework import generics, status
from cars_api import models, serializers
from django.db import IntegrityError
from rest_framework.response import Response


class CarsListView(generics.ListCreateAPIView):
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