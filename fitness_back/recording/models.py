from django.db import models
from users.models import Client
from schedules.models import Time, Zal, Schedule
from trainers.models import Coach
# Create your models here.


class Appointment(models.Model):  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField(max_length=200)

    def __str__(self):
        return f"Appointment for {self.client.full_name} with {self.coach.full_name} at {self.zal.name} | {self.time.start_time} - {self.time.end_time} on {self.date}"
