# from django.test import TestCase, client
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.reverse import reverse

# # Create your tests here.
# class BaseTest(APITestCase):
#   '''
#   Base test case for all test cases
#   '''
#   client=APIClient()
  
#   def setUp(self):
#     '''
#     test method for all settings
#     '''
#     self.login_url = reverse("authentication:login")

import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import *
from .serializers import *


# Registration Test Case
class RegistrationTestCase(APITestCase):
  def test_registration(self):
    reg_info = {"username": "test", "first_name":"kevson", "last_name": "kim", "email": "kevson@gmail.com", "password": "pass123"}
    response = self.client.post("/api/register/", reg_info)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
# Login Test Case
class LoginTestCase(APITestCase):
  def test_login(self):
    # Register a user test case
    reg_info = {"username": "test", "first_name":"kevson", "last_name": "kim", "email": "kevson@gmail.com", "password": "pass123"}
    response = self.client.post("/api/register/", reg_info)
    # Test logining in with the registered credentials
    login_info = {"username": "test", "password": "pass123"}
    response = self.client.post("/api/login/", login_info)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


    
    