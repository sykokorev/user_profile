from django.shortcuts import render
from django.http import Http404

from .models import Exercise
from .models import Equipment


def exercises(request):
    data = Exercise.objects.all()
    if data:
        context = {
            'exercises': data,
        }
        return render(request, 'workout.html', context)
    else:
        return Http404('No data')


def exercise_detail(request, exercise: str):
    exercises = Exercise.objects.filter(name=exercise).all()
    if exercises:
        context = {
            'exercise': exercises[0].name,
            'level': Exercise.Level(exercises[0].level).label,
            'type': exercises[0].ex_type,
            'equipments': [equipment for equipment in exercises[0].equipment.all()]
        }
        return render(request, 'exercise_detail.html', context)
    else:
        return Http404('No data')


def equipments(request):
    equipment_objs = Equipment.objects.all()
    equipments = []
    for equipment in equipment_objs:
        equipments.append(
            {
                'equipment': equipment.name,
                'description': equipment.description
            }
        )
    context = {'equipments': equipments}
    return render(request, 'equipments.html', context)


def equipment_detail(request, equipment: str):
    equipment = Equipment.objects.filter(name=equipment).all()
    if not equipment:
        return Http404('No data')
    elif equipment:
        context = {
            'equipment': equipment[0].name,
            'description': equipment[0].description
        }
        return render(request, 'equipment_detail.html', context)
