from django.urls import path
from .views import CreateFisheryView, FisheryList

app_name = 'fishery'

urlpatterns = [
    # ... inne URL-e
    path('create/', CreateFisheryView.as_view(), name='fishery-create'),
    path('all/', FisheryList.as_view(), name='fishery-list'),
]