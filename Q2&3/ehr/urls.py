from django.urls import path
from .views import PatientList

urlpatterns = [
    path('', PatientList.as_view(), name='patient-list'),
]
