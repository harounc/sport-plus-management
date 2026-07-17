from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Joueur(models.Model):
    GARDIEN, DEFENSEUR, MILIEU, ATTAQUANT = "Gardien", "Défenseur", "Milieu", "Attaquant"
    POSTES = [(GARDIEN, "Gardien"), (DEFENSEUR, "Défenseur"), (MILIEU, "Milieu"), (ATTAQUANT, "Attaquant")]
    nom = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True)
    poste = models.CharField(max_length=20, choices=POSTES)
    date_naissance = models.DateField()
    club_actuel = models.CharField(max_length=150)
    nationalite = models.CharField(max_length=100)
    pied_fort = models.CharField(max_length=20, choices=[("Droit", "Droit"), ("Gauche", "Gauche"), ("Ambidextre", "Ambidextre")])
    photo = models.ImageField(upload_to="joueurs/", blank=True)
    video = models.URLField(blank=True)
    description = models.TextField()
    matchs = models.PositiveIntegerField(default=0)
    buts = models.PositiveIntegerField(default=0)
    passes_decisives = models.PositiveIntegerField(default=0)
    mis_en_avant = models.BooleanField(default=False)
    ordre = models.PositiveSmallIntegerField(default=0)
    class Meta: ordering = ["ordre", "nom"]
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.nom)
        super().save(*args, **kwargs)
    @property
    def age(self):
        from django.utils.timezone import localdate
        today = localdate()
        return today.year - self.date_naissance.year - ((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))
    @property
    def fallback_image(self): return f"images/generated/player-{self.ordre + 1}.webp"
    def get_absolute_url(self): return reverse("joueurs:detail", args=[self.slug])
    def __str__(self): return self.nom
