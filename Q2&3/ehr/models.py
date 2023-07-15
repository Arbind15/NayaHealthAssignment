from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    doctors = models.ManyToManyField(Doctor)
    medicines = models.ManyToManyField(Medicine)
    prescriptions = models.ManyToManyField("Prescription", related_name='patients')

    def __str__(self):
        return self.name


class Prescription(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.medicine}"
