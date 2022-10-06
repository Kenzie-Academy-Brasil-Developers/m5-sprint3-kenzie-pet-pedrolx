import math
from unittest import TestCase
from animals.models import Animal, Choices
from groups.models import Group
from traits.models import Trait


class AnimalModelTest(TestCase):
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

    def testing_field_choices(self):
        self.assertEqual(type(self.created_animal.sex), str)
        self.assertIn(self.created_animal.sex, Choices)

    def testing_method_age_to_human(self):
        self.assertEqual(16 * math.log(self.animal['age']) + 31, self.created_animal.convert_dog_age_to_human_years())

    def testing_fields(self):
        self.assertIs(type(self.created_animal.name), str)
        self.assertIs(type(self.created_animal.weight), float)

    def testing_animal_created_instance(self):
        self.assertIsInstance(self.created_animal, Animal)
