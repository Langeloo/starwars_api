from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"
    
    class Meta:
        db_table = "auth_user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        
## Star Wars API
class Planet(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    climate = models.CharField(max_length=255)
    terrain = models.CharField(max_length=255)
    population = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "planet"
        verbose_name = "Planet"
        verbose_name_plural = "Planets"
        
class Character(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    height = models.CharField(max_length=255)
    mass = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    skin = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        db_table = "character"
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        
class Film(models.Model):
    title = models.CharField(max_length=255, primary_key=True)
    episode_id = models.CharField(max_length=255)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)
    characters = models.ManyToManyField(Character, related_name="characters")
    planets = models.ManyToManyField(Planet, related_name="planets")
    release_date = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = "film"
        verbose_name = "Film"
        verbose_name_plural = "Films"