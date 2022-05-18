from django.db import models


class ExerciseType(models.Model):
    name = models.CharField(
        verbose_name='Exercise type',
        max_length=127,
        null=False,
        unique=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Equipment(models.Model):

    name = models.CharField(
        verbose_name='Equipment',
        max_length=255,
        null=False,
        unique=True
    )
    description = models.TextField(
        verbose_name='Equipment Description',
        max_length=1023,
        null=True,
        unique=False
    )

    def __str__(self):
        return self.name


class Exercise(models.Model):

    class Level(models.IntegerChoices):
        BEGINNER = 0, 'Beginner'
        INTERMEDIATE = 1, 'Intermediate'
        UPPER_INTERMEDIATE = 2, 'Upper-Intermediate'
        ADVANCED = 3, 'Advanced'

    name = models.CharField(
        verbose_name='Exercise',
        max_length=255,
        null=False,
        unique=True
    )
    level = models.SmallIntegerField(
        verbose_name='Exercise Level',
        choices=Level.choices,
        default=0
    )
    ex_type = models.ForeignKey(
        'ExerciseType',
        verbose_name='Exercise Type',
        on_delete=models.CASCADE,
    )
    equipment = models.ManyToManyField(
        'Equipment',
        verbose_name='Equipment Needed',
    )

    class Meta:
        ordering = ('name', 'level')

    def __str__(self):
        return f'Exercise - {self.name}. Level - {self.Level(self.level).label}'
