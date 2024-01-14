from django.db import models
from user.models import User

# Create your models here.


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciver')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    date_sent = models.DateField(auto_now=True)
