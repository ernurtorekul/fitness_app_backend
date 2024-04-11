"""
URL configuration for fitness_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import user_login
from rest_framework.routers import DefaultRouter

from users.views import ClientListCreateAPIView, ClientRetrieveUpdateDestroyAPIView
from trainers.views import CoachListCreateAPIView, CoachRetrieveUpdateDestroyAPIView
from schedules.views import ScheduleListCreateAPIView, ScheduleRetrieveUpdateDestroyAPIView
from recording.views import AppointmentViewSet


router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='user_login'),

    path('api/users/', ClientListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>', ClientRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),

    path('api/trainers/', CoachListCreateAPIView.as_view(), name='trainer-list-create'),
    path('api/users/<int:pk>', CoachRetrieveUpdateDestroyAPIView.as_view(), name='trainer-detail'),

    path('api/schedules/', ScheduleListCreateAPIView.as_view(), name='schedule-list-create'),
    path('api/users/<int:pk>', ScheduleRetrieveUpdateDestroyAPIView.as_view(), name='schedule-detail'),

    path('api/', include(router.urls))
]


