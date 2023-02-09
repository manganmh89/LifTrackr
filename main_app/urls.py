from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('workouts/', views.workouts_index, name='index'),
    path('workouts/<int:workout_id>/', views.workouts_detail, name='detail'),
    path('workouts/create/', views.WorkoutCreate.as_view(), name='workouts_create'),
    path('workouts/<int:pk>/update/', views.WorkoutUpdate.as_view(), name='workouts_update'),
    path('workouts/<int:pk>/delete/', views.WorkoutDelete.as_view(), name='workouts_delete'),
    path('workouts/<int:workout_id>/logging/', views.logging, name='logging'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/', views.ExerciseIndex.as_view(), name='exercises_index'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('workouts/<int:workout_id>/add_exercise/<int:exercise_id>/', views.add_exercise, name='add_exercise'),
    path('workouts/<int:workout_id>/remove_exercise/<int:exercise_id>/', views.remove_exercise, name='remove_exercise'),
    # path('loggings/create/', views.LoggingCreate.as_view(), name='loggings_create'),
    # path('loggings/', views.ExerciseIndex.as_view(), name='loggings_index'),
    # path('loggings/<int:pk>/', views.ExerciseDetail.as_view(), name='loggings_detail'),
    # path('loggings/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='loggings_update'),
    # path('loggings/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='loggings_delete'),
    # path('workouts/<int:workout_id>/add_logging/<int:logging_id>/', views.add_logging, name='add_logging'),
    # path('workouts/<int:workout_id>/remove_logging/<int:logging_id>/', views.remove_logging, name='remove_logging'),
    path('accounts/signup/', views.signup, name='signup'),
]