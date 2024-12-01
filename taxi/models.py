from django.db import models

class Taxi(models.Model):
    STATUS_CHOICE = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('under maintenance', 'Hyundai ')
    ]
    taxi_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=100)




