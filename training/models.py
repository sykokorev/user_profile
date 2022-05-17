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

    LEVEL = [
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Upper-Intermediate'),
        (3, 'Advanced')
    ]

    name = models.CharField(
        verbose_name='Exercise',
        max_length=255,
        null=False,
        unique=True
    )
    level = models.SmallIntegerField(
        verbose_name='Exercise Level',
        choices=LEVEL,
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
        null=True
    )

    class Meta:
        ordering = ('name', 'level')

    def __str__(self):
        return f'{self.name} - {self.level}'
