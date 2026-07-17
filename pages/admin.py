from django.contrib import admin
from .models import Fondateur, MessageContact

@admin.register(Fondateur)
class FondateurAdmin(admin.ModelAdmin):
    list_display = ("nom", "role", "ordre")
    list_editable = ("ordre",)

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "sujet", "date_envoi", "traite")
    list_filter = ("traite", "date_envoi")
    search_fields = ("nom", "email", "sujet", "message")
    readonly_fields = ("nom", "email", "sujet", "message", "date_envoi")
