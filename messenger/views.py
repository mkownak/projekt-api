from rest_framework import generics,serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from .serializer import MessageSerializer
from user.models import User

# Create your views here.
class CreateMessageView(generics.CreateAPIView):
    queryset = models.Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(sender=self.request.user)

class MessageListView(generics.ListAPIView):
    queryset = models.Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.Message.objects.filter(reciver=self.request.user)