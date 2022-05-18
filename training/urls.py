from django.urls import path

from . import views


urlpatterns = [
    path('workout/', views.training, name='workout')
]
