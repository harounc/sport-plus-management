from django.shortcuts import get_object_or_404, render
from .models import Actualite
def list_news(request): return render(request, "actualites/list.html", {"actualites": Actualite.objects.filter(publie=True)})
def detail(request, slug): return render(request, "actualites/detail.html", {"article": get_object_or_404(Actualite, slug=slug, publie=True)})
