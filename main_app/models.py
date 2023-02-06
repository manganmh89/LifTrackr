from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    sets = models.IntegerField()
    reps = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('exercises_detail', kwargs={'pk': self.id})

class Workout(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'workout_id': self.id})


