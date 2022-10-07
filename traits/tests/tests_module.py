from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait
from django.forms.models import model_to_dict

class TraitsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.animal = {
        "name": "Beethoven",
        "age": 1,
        "weight": 30.5,
        "sex": "Macho",
        "group": {"name": "cão", "scientific_name": "canis familiaris"},
        "traits": [{"name": "peludo"}, {"name": "médio porte"}]
        }

        cls.group = cls.animal.pop('group')

        cls.traits = cls.animal.pop('traits')

        cls.created_group, _ = Group.objects.get_or_create(**cls.group)

        cls.created_animal = Animal.objects.create(**cls.animal, group=cls.created_group)

        cls.created_traits = {}

        for trait in cls.traits:
            new_trait, _ = Trait.objects.get_or_create(**trait)
            cls.created_animal.traits.add(new_trait)

    def testing_fields(self):
        expected = str

        traits = self.created_animal.traits.all()

        for trait in traits:
            self.assertIs(type(trait.name), expected)

    def testing_instance(self):
        expected = Trait

        traits = self.created_animal.traits.all()

        for trait in traits:
            self.assertIsInstance(trait, Trait)
