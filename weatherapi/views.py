import json

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .helper import normalize


# Create your views here.
class WeatherForecast(APIView):
    def get(self, request, q_param):
        q_param = normalize(q_param) # usuniecie polskich znakow przy podaniu miasta
        api_key = '964ee817965d4c4db87163320240301'
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={q_param}&days=7'

        response = requests.get(url)

        if response.status_code != 200:
            return Response({'error'}, status=response.status_code)
        else:
            data = response.json()
            return Response(data, status=status.HTTP_200_OK)

class WeatherLunar(APIView):
    def get(self, request, q_param):
        q_param = normalize(q_param) # usuniecie polskich znakow przy podaniu miasta
        api_key = '964ee817965d4c4db87163320240301'
        url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={q_param}&days=7'

        response = requests.get(url)


        if response.status_code != 200:
            return Response({'error'}, status=response.status_code)
        else:

            data = response.json()
            new_response = {}

            forecastlocation = data['location']
            forecastdays = data['forecast']['forecastday']
            new_response['location'] = forecastlocation

            for day in forecastdays:
                date = day['date']
                astro = day['astro']

                new_response[date] = {
                    'astro': astro
                }

            return Response(new_response, status=status.HTTP_200_OK)
