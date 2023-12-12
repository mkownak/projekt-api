from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from fishery.models import Fishery
from user.models import User
from django.urls import reverse

# Create your tests here.
FISHERY_CREATE_URL = reverse('fishery:fishery-create')
FISHERY_ALL_URL = reverse('fishery:fishery-list')

class FisheryTests(TestCase):
    def setUp(self):
        self.public_client = APIClient()
        self.user = User.objects.create(
            email='testuser@example.com',
            password='testpassword',
            username='testuser'
        )
        self.public_client.force_authenticate(user=self.user)

    def test_create_fishery_successful(self):
        """Test creating a new fishery"""
        payload = {
            'name': 'Test',
            'description': 'Testariusz',
            'category': 'River',
            'latitude': 50.12345,
            'longitude': 19.67890,
        }

        res = self.public_client.post(FISHERY_CREATE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        #print(res.content)
        name = res.data.get('name')
        fishery = Fishery.objects.get(name=name)
        fishery.status = "Accepted"
        fishery.save()

        updated_fishery = Fishery.objects.get(name=name)
        self.assertEqual(updated_fishery.status, 'Accepted')

    def test_list_accepted_fisheries(self):
        """Test listing accepted fisheries"""
        Fishery.objects.create(
            name='Fishery1',
            description='Description1',
            category='River',
            latitude=50.123,
            longitude=19.678,
            status='Accepted',
            user_added=self.user
        )
        Fishery.objects.create(
            name='Fishery2',
            description='Description2',
            category='Lake',
            latitude=51.123,
            longitude=20.678,
            status='Accepted',
            user_added=self.user
        )

        res = self.public_client.get(FISHERY_ALL_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)