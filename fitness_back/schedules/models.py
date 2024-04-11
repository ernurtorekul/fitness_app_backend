from django.db import models


class Zal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Time(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"
    

class Schedule(models.Model):
    zal = models.ForeignKey(Zal, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.zal.name} | {self.time} | {self.date}"