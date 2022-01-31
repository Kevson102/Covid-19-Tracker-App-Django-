from django.test import TestCase

# Create your tests here.
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

class HealthCheckTestCase(APITestCase):
  # Test post request
    def test_answers_post(self):
        question = {"question": "Do you have nasal congestion"}
        answers = json.dumps(answers)
        patient = requests.post("http://127.0.0.1:8000/api/healthcheck/", answers_data)
        self.assertEqual(patient.status_code, status.HTTP_200_OK)
    # Test get request
    def test_answers_get(self):
        
        found_answers = self.client.get("http://127.0.0.1:8000/api/response/")
        self.assertEqual(found_answers.status_code, status.HTTP_200_OK)