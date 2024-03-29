from django.urls import path
from .views import CreateMessageView, MessageListView

app_name = 'messenger'

urlpatterns = [
    path('send/', CreateMessageView.as_view(), name='message-send'),
    path('recived/', MessageListView.as_view(), name='message-recived')
]
