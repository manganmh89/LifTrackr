from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Workout, Exercise
from .forms import LoggingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def workouts_index(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'workouts/index.html', { 'workouts': workouts })

@login_required
def workouts_detail(request, workout_id):
    workout = Workout.objects.get(id=workout_id)
    logging_form = LoggingForm()
    exercises_workout_dn_have = Exercise.objects.exclude(id__in=workout.exercises.all().values_list('id'))
    return render(request, 'workouts/detail.html', {
        'workout': workout,
        'logging_form': logging_form,
        'exercises': exercises_workout_dn_have
    })

@login_required
def logging(request, workout_id):
  form = LoggingForm(request.POST)
  if form.is_valid():
    new_logging = form.save(commit=False)
    new_logging.workout_id = workout_id
    new_logging.save()
  return redirect('detail', workout_id=workout_id)

@login_required
def add_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.add(exercise_id)
  return redirect('detail', workout_id=workout_id)

@login_required
def remove_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.remove(exercise_id)
  return redirect('detail', workout_id=workout_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    pass
  form = UserCreationForm(request.POST)
  if form.is_valid():
    user = form.save()
    login(request, user)
    return redirect('index')
  else:
    error_message = 'invalid credentials'
    form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error_message': error_message
  })

class WorkoutCreate(LoginRequiredMixin, CreateView):
  model = Workout
  fields = ('name', 'target', 'description')
  success_url = '/workouts/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WorkoutUpdate(LoginRequiredMixin, UpdateView):
  model = Workout
  fields = ('name', 'target', 'description')

class WorkoutDelete(LoginRequiredMixin, DeleteView):
  model = Workout
  success_url = '/workouts/'

class ExerciseIndex(LoginRequiredMixin, ListView):
  model = Exercise

class ExerciseDetail(LoginRequiredMixin, DetailView):
  model = Exercise

class ExerciseCreate(LoginRequiredMixin, CreateView):
  model = Exercise
  fields = '__all__'

class ExerciseUpdate(LoginRequiredMixin, UpdateView):
  model = Exercise
  fields = '__all__'

class ExerciseDelete(LoginRequiredMixin, DeleteView):
  model = Exercise
  success_url = '/exercises/'