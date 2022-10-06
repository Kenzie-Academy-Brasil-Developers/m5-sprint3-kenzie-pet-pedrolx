from unittest import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait
from django.forms.models import model_to_dict

class TraitsModelTest(TestCase):
    animal = {
    "name": "Beethoven",
    "age": 1,
    "weight": 30.5,
    "sex": "Macho",
    "group": {"name": "cão", "scientific_name": "canis familiaris"},
    "traits": [{"name": "peludo"}, {"name": "médio porte"}]
    }

    group = animal.pop('group')

    traits = animal.pop('traits')

    created_group, _ = Group.objects.get_or_create(**group)

    created_animal = Animal.objects.create(**animal, group=created_group)

    created_traits = {}

    for trait in traits:
        new_trait, _ = Trait.objects.get_or_create(**trait)
        created_animal.traits.add(new_trait)