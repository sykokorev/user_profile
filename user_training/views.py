from django.shortcuts import render
from django.http import Http404

from user.models import UserProfile
from training.models import Exercise
from .models import Training


def index(request):
    user = UserProfile.objects.get(pk=request.user.id)
    request_trainings = Training.objects.filter(user_id=request.user.id)
    trainings = []
    for training in request_trainings:
        trainings.append(
            {
                'training_id': training.id,
                'training': training.name
            }
        )

    context = {
        'user': user.name,
        'email': user.email,
        'is_superuser': user.is_superuser,
        'weight': user.weight,
        'height': user.height,
        'trainings': trainings
    }
    return render(request, 'index.html', context)


def workout_details(request, id):
    training = Training.objects.get(
        user_id=request.user.id, pk=id
    )
    if not training:
        return Http404('Training has not been found.')
    elif training:
        context = {
            'training': training.name,
            'exercises': training.exercises.all()
        }
        return render(request, 'details.html', context)
