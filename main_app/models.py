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
    exercises = models.ManyToManyField(Exercise)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'workout_id': self.id})

class Logging(models.Model):
    EFFORTS = (
        ('*', '1 Star'),
        ('**', '2 Star'),
        ('***', '3 Star'),
        ('****', '4 Star'),
        ('*****', '5 Star'),
    )
    date = models.DateField('workout date')
    effort = models.CharField(max_length=5, choices=EFFORTS, default=EFFORTS[0][0], verbose_name='effort given')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_effort_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)