from rest_framework import serializers
from .models import Zal, Time, Schedule


# used the nested method below

class ZalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zal
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    zal = ZalSerializer()
    time = TimeSerializer()
    class Meta:
        model = Schedule
        fields = '__all__'