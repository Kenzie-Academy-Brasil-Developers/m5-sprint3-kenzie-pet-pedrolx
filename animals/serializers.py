from rest_framework import serializers
from animals.exceptions import NonUpdatableKeyError
from animals.models import Animal, Choices
from groups.models import Group
from traits.models import Trait
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Choices.choices,
        default=Choices.UNINFORMED,
        )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
    age_in_human_years = serializers.SerializerMethodField(read_only=True)

    def get_age_in_human_years(self, obj: Animal):
        return obj.convert_dog_age_to_human_years()
    
    def create(self, validated_data: dict):

        group_data = validated_data.pop('group')
        traits_data = validated_data.pop('traits')

        new_group, _ = Group.objects.get_or_create(**group_data)

        animal_created = Animal.objects.create(**validated_data, group=new_group)

        for trait in traits_data:
            new_trait, _ = Trait.objects.get_or_create(**trait)
            animal_created.traits.add(new_trait)
        animal_created.save()

        return animal_created

    def update(self, instance: Animal, validated_data: dict):
        errors = {}
        valid_data = {
            "traits": Trait,
            "group": Group,
            "sex": str
        }

        for data in valid_data.keys():
            if data in validated_data:
                msg = {f"{data}": f"You can not update {data} property."}
                errors.update(msg)
        
        if len(errors) > 0:
                raise NonUpdatableKeyError(errors)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
        
