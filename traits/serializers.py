from rest_framework import serializers

from animals.serializers import AnimalSerializer


class TraitSerializer(serializers.Serializer): 
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)