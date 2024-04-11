from django.shortcuts import render
from rest_framework import generics
from .models import Coach
from .serializers import CoachSerializer
# Create your views here.


class CoachListCreateAPIView(generics.ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class CoachRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer



