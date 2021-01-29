from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
from .models import Status

admin.site.register(Status)
