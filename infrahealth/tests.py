import json
import requests

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.parsers import JSONParser

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

# Healthcheck test case
class HealthCheckTestCase(APITestCase):
  # Test post request
  def test_healthcheck_post(self):
    question = {"question": "Do you have nasal congestion"}
    question_data = json.dumps(question)
    response = requests.post("http://127.0.0.1:8000/api/healthcheck/", question_data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
  # Test get request
  def test_healthcheck_get(self):
    # get the saved question
    found_question = self.client.get("http://127.0.0.1:8000/api/healthcheck/")
    self.assertEqual(found_question.status_code, status.HTTP_200_OK)

  
    