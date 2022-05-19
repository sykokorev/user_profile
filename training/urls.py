from django.urls import path

from . import views


urlpatterns = [
    path('workout/', views.exercises, name='exercises'),
    path('workout/<str:exercise>', views.exercise_detail, name='exercise_detail'),
    path('workout/equipments/', views.equipments, name='equipments'),
    path('workout/equipments/<str:equipment>', views.equipment_detail, name='equipment_detail')
]
