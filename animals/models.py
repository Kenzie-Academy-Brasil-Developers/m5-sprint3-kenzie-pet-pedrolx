from email.policy import default
from random import choices
from django.db import models

class Choices(models.TextChoices):
    MALE = 'Macho'
    FEMALE = 'Fêmea'
    UNINFORMED = 'Não Informado'

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15, choices=Choices.choices, default=Choices.UNINFORMED,
    )

    group = models.ForeignKey(
        'groups.Group', 
        on_delete=models.CASCADE,
        related_name='animals',
        )

    traits = models.ManyToManyField(
        'traits.Trait', related_name='traits',
        )
