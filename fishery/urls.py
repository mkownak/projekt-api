from django.urls import path
from .views import CreateFisheryView, FisheryList, PicturesList, CreatePictureView, RetriveFishery

app_name = 'fishery'

urlpatterns = [
    # ... inne URL-e
    path('create/', CreateFisheryView.as_view(), name='fishery-create'),
    path('found/', FisheryList.as_view(), name='fishery-list'),
    path('<int:pk>/pictures/', PicturesList.as_view(), name='fishery-list-pictures'),
    path('add_picture', CreatePictureView.as_view(), name='fishery-add-picture'),
    path('<int:pk>', RetriveFishery.as_view(), name='fishery-retrive')
]