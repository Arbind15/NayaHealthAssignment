from rest_framework import serializers
from .models import Patient, Prescription, Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class PrescriptionSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer()

    class Meta:
        model = Prescription
        fields = ('medicine', 'dosage')


class PatientSerializer(serializers.ModelSerializer):
    prescriptions = PrescriptionSerializer(many=True)

    class Meta:
        model = Patient
        fields = ('name', 'age', 'prescriptions')
