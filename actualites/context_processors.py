from .models import Actualite
def site_news(request):
    return {"ticker_news": Actualite.objects.filter(publie=True)[:4]}
