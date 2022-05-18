from django.db import models

from training.models import Exercise
from user.models import UserProfile


class Training(models.Model):
    name = models.CharField(
        verbose_name='Workout Name',
        max_length=125,
    )
    user_id = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE
    )
    exercises = models.ManyToManyField(Exercise)

    class Meta:
        ordering = ['user_id']

    def __str__(self):
        return f'User ID {self.user_id.id}. Name {self.user_id.name}. Training name - {self.name}'
