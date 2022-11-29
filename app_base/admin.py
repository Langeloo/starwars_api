from django.contrib import admin
from .models import User, Planet, Character, Film

# Register your models here.
admin.site.register(User)
admin.site.register(Planet)
admin.site.register(Character)
admin.site.register(Film)
