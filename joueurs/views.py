from django.shortcuts import get_object_or_404, render
from .models import Joueur
def list_players(request): return render(request, "joueurs/list.html", {"joueurs": Joueur.objects.all()})
def detail(request, slug): return render(request, "joueurs/detail.html", {"joueur": get_object_or_404(Joueur, slug=slug)})
