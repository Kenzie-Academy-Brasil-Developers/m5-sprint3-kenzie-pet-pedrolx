from rest_framework import serializers

from animals.models import Animal, Choices
from groups.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Choices.choices,
        default=Choices.UNINFORMED,
        )

    def create(self, validated_data: dict):
        return Animal.objects.create(**validated_data)

    def update(self, instance: Animal, validated_data: dict):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.sex = validated_data.get(' sex', instance.sex)

        instance.save()

        return instance