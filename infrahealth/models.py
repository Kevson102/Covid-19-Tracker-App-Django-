from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
   location_name = models.CharField(max_length=30)
   Geo_location = models.CharField(max_length=30)
   
   def __str__(self):
       return self.location_name
     
     
class Patient(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    Location= models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
      
class HealthCheckQuestions(models.Model):
  question = models.CharField(max_length=200)
  
  def __str__(self):
    return self.question
    
class answer(models.Model):
  question = models.ForeignKey(HealthCheckQuestions, on_delete=models.CASCADE)
  answer = models.CharField(max_length=20)
  
  def __str__(self):
    return self.answer
     
# class HealthCheck(models.Model):
#    Have_you_lost_smell_or_test = models.BooleanField()
#    Do_you_have_a_sore_throat = models.BooleanField()
#    Are_you_experiencing_fatigue= models.BooleanField()
#    Do_you_have_a_cough= models.BooleanField()
#    Do_you_have_difficulties_in_breathing= models.BooleanField()
#    Do_you_have_a_fever= models.BooleanField()
#    Do_you_have_chills= models.BooleanField()
#    Do_you_have_a_headache= models.BooleanField()
#    Do_you_have_muscle_aches= models.BooleanField()
#    Do_you_have_nasal_congestion= models.BooleanField()
#    Are_you_experiencing_nausea= models.BooleanField()
#    Are_you_experiencing_any_vomiting= models.BooleanField()
#    Do_you_have_diarrhea= models.BooleanField()
#    Close_contact_with_an_infected_person= models.BooleanField()
#    Patient=models.ForeignKey(Patient, on_delete= models.CASCADE)
   
#    def __str__(self):
#        return self.Patient