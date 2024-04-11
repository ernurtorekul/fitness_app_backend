from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class BaseUser(AbstractUser):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    number = models.CharField(max_length=15)
    email = models.EmailField()

    ROLE_CHOICES = [
        ('coach', 'Coach'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
 
    def __str__(self):
        return f"{self.name} {self.surname} - {self.get_role_display()}"


class Client(BaseUser):
    tarif_options = [
        ('1', 'Tarif 1'),
        ('2', 'Tarif 2'),
        ('3', 'Tarif 3'),
    ]
    tarif = models.CharField(max_length=1, choices=tarif_options)
    weight = models.FloatField()
    height = models.FloatField()


