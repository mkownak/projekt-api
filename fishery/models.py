from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Fishery(models.Model):
    categories = (
        ('', 'wybierz kategorie'),
        ('River', 'Rzeka'),
        ('Lake', 'Jezioro'),
        ('Pond', 'Staw'),
        ('Sea', 'Morze')
    )

    statuses = (
        ('Pending', 'Oczekujace'),
        ('Accepted', 'Zaakceptowane'),
        ('Discarded', 'Odrzucone')
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=categories)
    latitude = models.FloatField()
    longitude = models.FloatField()
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=statuses, default='Pending')
