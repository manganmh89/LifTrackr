from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
# from .models import Workout, Exercise, Log
# from .forms import WorkoutForm, ExerciseForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
