from django.contrib import admin
from .models import Actualite
@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ("titre", "date", "publie")
    list_filter = ("publie", "date")
    search_fields = ("titre", "extrait", "contenu")
    prepopulated_fields = {"slug": ("titre",)}
