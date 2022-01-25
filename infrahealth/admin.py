from django.contrib import admin

from infrahealth.models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Patient)
admin.site.register(HealthCheckQuestions)

