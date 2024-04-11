from django.contrib import admin
from users.models import BaseUser
from trainers.models import Coach



# Register your models here.

admin.site.register(BaseUser)
admin.site.register(Coach)

