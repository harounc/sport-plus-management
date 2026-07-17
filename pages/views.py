from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from actualites.models import Actualite
from joueurs.models import Joueur
from .forms import ContactForm
from .models import Fondateur, MessageContact

SERVICES = [
    ("rep", "Représentation", "Négociation de contrats, défense des intérêts du joueur auprès des clubs et partenaires."),
    ("placement", "Placement", "Identification des opportunités et mise en relation avec des clubs adaptés au profil et au projet de carrière."),
    ("career", "Accompagnement de carrière", "Suivi personnalisé, préparation des étapes clés et conseil sur les choix sportifs."),
    ("image", "Image & visibilité", "Valorisation de l’image du joueur, relations médias et développement de sa notoriété."),
]

def home(request):
    return render(request, "pages/home.html", {"services": SERVICES, "joueurs": Joueur.objects.filter(mis_en_avant=True)[:4], "actualites": Actualite.objects.all()[:3]})
def about(request): return render(request, "pages/about.html", {"fondateurs": Fondateur.objects.all()})
def services(request): return render(request, "pages/services.html", {"services": SERVICES})
def legal(request): return render(request, "pages/legal.html")
def privacy(request): return render(request, "pages/privacy.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MessageContact.objects.create(nom=data["nom"], email=data["email"], sujet=data["sujet"], message=data["message"])
            send_mail(f"Contact SPM — {data['sujet'] or 'Sans sujet'}", f"Nom: {data['nom']}\nE-mail: {data['email']}\n\n{data['message']}", settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL], fail_silently=True)
            request.session["contact_sent"] = True
            return redirect("pages:contact")
    else:
        form = ContactForm()
    sent = request.session.pop("contact_sent", False)
    return render(request, "pages/contact.html", {"form": form, "sent": sent})
