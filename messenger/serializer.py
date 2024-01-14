from rest_framework import serializers

from user.serializer import UserSerializer
from . import models


class MessageSerializer(serializers.ModelSerializer):
    date_sent = serializers.DateField(read_only=True, format='%d %B %Y')
    sender = UserSerializer(read_only=True)

    class Meta:
        model = models.Message
        fields = (
            'sender',
            'reciver',
            'subject',
            'content',
            'date_sent',
        )
