from django.db import models
from django.urls import reverse
from django.utils.text import slugify
class Actualite(models.Model):
    titre = models.CharField(max_length=220)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField()
    image = models.ImageField(upload_to="actualites/", blank=True)
    extrait = models.TextField(max_length=350)
    contenu = models.TextField()
    publie = models.BooleanField(default=True)
    class Meta: ordering = ["-date"]
    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    def get_absolute_url(self): return reverse("actualites:detail", args=[self.slug])
    @property
    def fallback_image(self):
        mapping = {"jean-eudes-aka-signe-au-stade-rennais": 1, "sport-plus-management-partenaire-abidjan-cup": 2, "didier-nguessan-buteur-decisif": 3}
        return f"images/generated/news-{mapping.get(self.slug, 1)}.webp"
    def __str__(self): return self.titre
