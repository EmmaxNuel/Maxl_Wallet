from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


from .models import User

class TestSignUp(TestCase):
    #arrange
    #act
    #assert

    def setUp(self):
        self.url = reverse("register")
        self.data = {
            "first_name": "Emmanuel",
            "last_name": "Olatunji",
            "email": "olatunjie335@gmail.com",
            "phone": "07046708198",
            "password":"EMmax_nuel",

        }

    def test_signup_returns_201(self):
        data = {
            "first_name": "Emmanuel",
            "last_name": "Isolation",
            "email": "olatunjie335@gmail.com",
            "phone": "07046708198",
            "password":"qwerty",
            "username":"Emmax_nuel"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_signup_returns_400(self):
        data = {
            "first_name": "Emmanuel",
            "last_name": "Olatunji",
            "email": "olatunjie335",
            "phone": "08198",
            "password":"qwerty",
            "username":"Emmax_nuel"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_login_returns_200(self):


        response = self.client.post(self.url, self.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        login_url = reverse('login')
        login_data = {
            "email":"olatunjie335@gmail.com",
            "password":"qwerty"
        }

        response1 = self.client.post(login_url, login_data)

        # self.assertEqual(response1.status_code, status.HTTP_200_OK)


    def test_login_with_invalid_details_returns_400(self):
        response = self.client.post(self.url, self.data)
        login_url = reverse('login')
        login_data = {
            "email":"olatunjie335",
            "password":""

        }

        response4 = self.client.post(login_url, login_data)
        self.assertEqual(response4.status_code, status.HTTP_400_BAD_REQUEST)
