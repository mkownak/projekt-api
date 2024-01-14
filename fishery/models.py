from django.db import models
from user.models import User


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

    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateField(auto_now=True)
    user_added = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    fishery = models.ForeignKey(Fishery, null=True, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='uploads/')
