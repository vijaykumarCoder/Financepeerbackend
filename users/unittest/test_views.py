import imp
from urllib import response
from rest_framework import status
from django.urls import reverse
from .test_setup import TestSetUp
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.test import APIClient




class TestViews(TestSetUp):

    def test_user_can_not_login_correctly(self):
        res = self.client.post(self.login_url,self.user_data,format="multipart")
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)

    def test_user_can_login_correctly(self):
        url = reverse('register')
        u = User.objects.create_user(username='Hi', email='hi@gmail.com')
        u.set_password('Hi@123')
        u.is_active = False
        u.save()

        resp = self.client.post(url, {'email':'hi@gmail.com', 'password':'Hi@123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        u.is_active = True
        u.save()

        resp = self.client.post(url, {'username':'Hi', 'password':'Hi@123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('token' in resp.data)
        token = resp.data['token']
        print(token)

        verification_url = reverse('login')
        resp = self.client.post(verification_url, {'token': token}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(verification_url, {'token': 'abc'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='JWT ' + 'abc')
        resp = client.get('login', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        resp = client.get('login', data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


        # response = self.client.post(self.login_url,self.user_data,format="json")
        # self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        # token = response.data['token']
        # self.client.credentials(HTTP_AUTHORIZATION='JWT {0}'.format(token))
        # response = self.client.get(reverse(self.login_url), data={'format': 'json'})
        # self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        # import pdb
        # pdb.set_trace() 
        # self.assertEqual(res.status_code, 200)