from django.contrib import admin

from infrahealth.models import HealthCheckQuestions, Location, Patient, answer

# Register your models here.
admin.site.register(Location)
admin.site.register(Patient)
admin.site.register(HealthCheckQuestions)
admin.site.register(answer)
