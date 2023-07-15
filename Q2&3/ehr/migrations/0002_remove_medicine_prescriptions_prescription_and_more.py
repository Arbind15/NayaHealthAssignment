# Generated by Django 4.2.3 on 2023-07-14 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ehr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='prescriptions',
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage', models.CharField(max_length=255)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ehr.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='prescriptions',
            field=models.ManyToManyField(related_name='patients', to='ehr.prescription'),
        ),
    ]
