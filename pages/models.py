from django.db import models

class Fondateur(models.Model):
    nom = models.CharField(max_length=150)
    role = models.CharField(max_length=180)
    photo = models.ImageField(upload_to="fondateurs/", blank=True)
    bio = models.TextField()
    ordre = models.PositiveSmallIntegerField(default=0)
    class Meta:
        ordering = ["ordre", "nom"]
    @property
    def fallback_image(self): return f"images/generated/founder-{min(self.ordre + 1, 3)}.webp"
    def __str__(self): return self.nom

class MessageContact(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    sujet = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)
    class Meta:
        ordering = ["-date_envoi"]
    def __str__(self): return f"{self.nom} — {self.sujet or 'Sans sujet'}"
