from django.db.models import ExpressionWrapper, FloatField, F
from django.shortcuts import render
from rest_framework import generics, authentication, permissions, status, serializers
from rest_framework.response import Response
from .models import Fishery
from .serializer import FisherySerializer, FisheryLocationFilterSerializer

# Create your views here.
class CreateFisheryView(generics.CreateAPIView): #dodawanie lowsika
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
        return Fishery.objects.filter(status='Accepted')
