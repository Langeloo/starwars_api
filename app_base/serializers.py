from rest_framework import serializers
from app_base.models import User, Planet, Character, Film

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = "__all__"
        
class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = "__all__"
        
class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"