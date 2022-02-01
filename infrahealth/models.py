from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)
    Geo_location = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

class HealthCheckQuestions(models.Model):
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Answer(models.Model):
    answer = models.BooleanField()
    date_responded = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(HealthCheckQuestions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.answer)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):

    hospital_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class MedicalTest(models.Model):
    age = models.IntegerField()
    pre_existing_condition = models.CharField(max_length=100)
    temperature = models.FloatField()
    nasal_swab_test = models.BooleanField()
    recommendation = models.CharField(max_length=100, null=True)
    date_tested = models.DateTimeField(auto_now=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nasal_swab_test)

