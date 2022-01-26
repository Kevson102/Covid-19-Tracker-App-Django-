from django.contrib import admin

from infrahealth.models import *

# Register your models here.
admin.site.register(Location)
admin.site.register(Patient)
admin.site.register(HealthCheckQuestions)
admin.site.register(Answer)
admin.site.register(Doctor)
admin.site.register(MedicalTest)
admin.site.register(Hospital)
