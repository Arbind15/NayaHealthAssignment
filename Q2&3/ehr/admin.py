from django.contrib import admin
from .models import Doctor, Patient, Prescription, Medicine
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Medicine)