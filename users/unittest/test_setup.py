import imp
from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.user_data = {
            "username":"Vivek",
            "password": "Vivek@123",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()