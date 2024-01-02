from django.db.models import ExpressionWrapper, FloatField, F
from django.shortcuts import render
from rest_framework import generics, authentication, permissions, status, serializers
from rest_framework.response import Response
from .models import Fishery, Picture
from .serializer import FisherySerializer, FisheryLocationFilterSerializer, PictureSerializer
import math
import rest_framework.response

# Create your views here.


class CreateFisheryView(generics.CreateAPIView):
    queryset = Fishery.objects.all()
    serializer_class = FisherySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        category = self.request.data.get('category')

        if category == '':
            raise serializers.ValidationError({"category": "Wybierz kategorie"})

        serializer.save(user_added=self.request.user)


class FisheryList(generics.ListAPIView):
    serializer_class = FisherySerializer

    def get_queryset(self):
        location_filter_serializer = FisheryLocationFilterSerializer(data=self.request.query_params)
        location_filter_serializer.is_valid(raise_exception=True)
        #print("Query Params:", self.request.query_params)

        user_lat = location_filter_serializer.validated_data.get('user_lat', None)
        user_lon = location_filter_serializer.validated_data.get('user_lon', None)
        max_radius = location_filter_serializer.validated_data.get('max_radius', None)

        fisheries = Fishery.objects.filter(status='Accepted')

        # dla punktow 0,0,0 wartosci przyjmuja false, warunek przez to sie nie spelnia trzeba 'is not none'
        # zamiast if user_lat and...

        # print(bool(user_lat))
        # print(bool(user_lon))
        # print(bool(max_radius))

        found_fisheries = []
        if user_lat is not None and user_lon is not None and max_radius is not None:
            #print('spelnione')
            for fishery in fisheries:
                lat = pow((user_lat - fishery.latitude), 2)
                lon = pow((user_lon - fishery.longitude), 2)
                dist = math.sqrt(lat+lon)
                #print(dist)

                if dist <= max_radius:
                    found_fisheries.append(fishery)

        return found_fisheries


class RetriveFishery(generics.RetrieveAPIView):
    queryset = Fishery.objects.all()
    serializer_class = FisherySerializer
    permission_classes = [permissions.IsAuthenticated]


class PicturesList(generics.ListAPIView):
    serializer_class = PictureSerializer

    def get_queryset(self):
        return Picture.objects.filter(fishery=self.kwargs.get('pk'))


class CreatePictureView(generics.CreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_added=self.request.user)