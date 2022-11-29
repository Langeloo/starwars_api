from django.urls import path
from .views import (
    ListCharacters,
    RegisterCharacter,
    ListPlanets,
    RegisterPlanet,
    ListFilms,
    RegisterFilm,
)

urlpatterns = [
    path("list-characters/", ListCharacters.as_view(), name=ListCharacters.class_name),
    path(
        "register-character/",
        RegisterCharacter.as_view(),
        name=RegisterCharacter.class_name,
    ),
    path("list-planets/", ListPlanets.as_view(), name=ListPlanets.class_name),
    path("register-planet/", RegisterPlanet.as_view(), name=RegisterPlanet.class_name),
    path("list-films/", ListFilms.as_view(), name=ListFilms.class_name),
    path("register-film/", RegisterFilm.as_view(), name=RegisterFilm.class_name),
]
