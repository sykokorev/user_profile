from django.urls import path

from . import views


urlpatterns = [
    path('workouts/', views.index, name='index'),
    path('workouts/<int:id>', views.workout_details, name='workouts')
]
