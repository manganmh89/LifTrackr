from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Workout, Exercise
# from .forms import LoggingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def workouts_index(request):
    return render(request, 'workouts/index.html', { 'workouts': workouts })

def workouts_detail(request):
    workout = Workout.objects.get(id=workout_id)
    logging_form = LoggingForm()
    exercises_workout_dn_have = Exercise.objects.exclude(id__in=workout.exercise.all().values_list('id'))
    return render(request, 'workouts/detail.html', {
        'workout': workout,
        'logging_form': logging_form,
        'exercises': exercises_workout_dn_have
    })

def logging(request, workout_id):
  form = LoggingForm(request.POST)
  if form.is_valid():
    new_logging = form.save(commit=False)
    new_logging.workout_id = workout_id
    new_logging.save()
  return redirect('detail', workout_id=workout_id)

def add_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.add(exercise_id)
  return redirect('detail', workout_id=workout_id)


def remove_exercise(request, workout_id, exercise_id):
  Workout.objects.get(id=workout_id).exercises.remove(exercise_id)
  return redirect('detail', workout_id=workout_id)

class WorkoutCreate(CreateView):
    model = Workout
    fields = ('__all__')
    success_url = '/workouts/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class WorkoutUpdate(UpdateView):
  model = Workout
  fields = ('__all__')

class WorkoutDelete(DeleteView):
  model = Workout
  success_url = '/workouts/'

class ExerciseIndex(ListView):
  model = Exercise

class ExerciseDetail(DetailView):
  model = Exercise

class ExerciseCreate(CreateView):
  model = Exercise
  fields = '__all__'

class ExerciseUpdate(UpdateView):
  model = Exercise
  fields = '__all__'

class ExerciseDelete(DeleteView):
  model = Exercise
  success_url = '/exercises/'