from django.db import models
from users.models import BaseUser   
# Create your models here.


class Coach(BaseUser):
    certifications_or_qualifications = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50)