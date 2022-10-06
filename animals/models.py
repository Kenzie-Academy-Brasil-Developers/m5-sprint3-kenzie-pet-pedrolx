from email.policy import default
import math
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
        null=True,
        )

    traits = models.ManyToManyField(
        'traits.Trait', related_name='traits',
        )

    def convert_dog_age_to_human_years(self) -> int:
        human_age = 16 * math.log(self.age) + 31
        return human_age
