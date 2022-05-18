from django.shortcuts import render


def training(request):
    context = {'user': 'Sergei'}
    return render(request, 'index.html')
