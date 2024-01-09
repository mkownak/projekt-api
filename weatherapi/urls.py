from django.urls import path
from .views import WeatherForecast, WeatherLunar

app_name = 'weather'

urlpatterns = [
    # ... inne URL-e
    path('forecast/<str:q_param>', WeatherForecast.as_view(), name='weekly-forecast'),
    path('lunar/<str:q_param>', WeatherLunar.as_view(), name='weekly-lunar'),
]