from django.shortcuts import render
from rest_framework import generics
from .models import Schedule    
from .serializers import ScheduleSerializer
# Create your views here.


class ScheduleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    # handling the nested serializers
    def perform_create(self, serializer):
        serializer.save(zal_data = self.request.data.get('zal'), time_data = self.request.data.get('time'))


class ScheduleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def perform_update(self, serializer):
        serializer.save(zal_data=self.request.data.get('zal'), time_data = self.request.data.get('time'))


