from django.contrib import admin

# Register your models here.
from .models import Workout, Exercise, Logging

# Register
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Logging)
