from django.test import TestCase
from animals.models import Animal
from groups.models import Group
from traits.models import Trait

class GroupModelTest(TestCase):
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

        for trait in cls.traits:
            new_trait, _ = Trait.objects.get_or_create(**trait)
            cls.created_animal.traits.add(new_trait)

    def testing_group_instance(self):
        self.assertIsInstance(self.created_animal.group, Group)

    def testing_groups_fields(self):
        self.assertIs(type(self.created_animal.group.name), str)
        self.assertIs(type(self.created_animal.group.scientific_name), str)
        len_name = len(self.created_animal.group.name)
        len_scientific_name = len(self.created_animal.group.scientific_name)
        self.assertLess(len_name, 21)
        self.assertLess(len_scientific_name, 51)