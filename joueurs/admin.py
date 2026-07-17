from django.contrib import admin
from .models import Joueur
@admin.register(Joueur)
class JoueurAdmin(admin.ModelAdmin):
    list_display = ("nom", "poste", "club_actuel", "mis_en_avant", "ordre")
    list_filter = ("poste", "mis_en_avant", "pied_fort")
    search_fields = ("nom", "club_actuel", "nationalite")
    prepopulated_fields = {"slug": ("nom",)}
