from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CharacterSerializer, PlanetSerializer, FilmSerializer
from app_base.models import Character, Planet, Film

# Create your views here.
class ListCharacters(APIView):
    class_name = "ListCharacters"

    def post(self, request):
        if "name" in request.data:
            characters = Character.objects.filter(name=request.data["name"])
        else:
            characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        for character in serializer.data:
            character["films"] = []
            for film in Film.objects.filter(characters__name=character["name"]):
                character["films"].append(film.title)
        return Response(serializer.data)


class RegisterCharacter(APIView):
    class_name = "RegisterCharacter"

    def post(self, request):
        serializer = CharacterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListPlanets(APIView):
    class_name = "ListPlanets"

    def post(self, request):
        if "name" in request.data:
            planets = Planet.objects.filter(name=request.data["name"])
        else:
            planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)
        for planet in serializer.data:
            planet["films"] = []
            for film in Film.objects.filter(planets__name=planet["name"]):
                planet["films"].append(film.title)
        return Response(serializer.data)


class RegisterPlanet(APIView):
    class_name = "RegisterPlanet"

    def post(self, request):
        serializer = PlanetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ListFilms(APIView):
    class_name = "ListFilms"

    def post(self, request):
        if "title" in request.data:
            films = Film.objects.filter(title=request.data["title"])
        else:
            films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)


class RegisterFilm(APIView):
    class_name = "RegisterFilm"

    def post(self, request):
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
