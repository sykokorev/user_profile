# Generated by Django 4.0.4 on 2022-05-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0004_alter_exercise_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='level',
            field=models.SmallIntegerField(choices=[(0, 'Beginner'), (1, 'Intermediate'), (2, 'Upper Intermediate'), (3, 'Advanced')], default=0, verbose_name='Exercise Level'),
        ),
    ]
