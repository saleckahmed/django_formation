from django.db import models
from authentification.models import Utilisateur


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Annonce(models.Model):
    titre = models.CharField(max_length=40)
    description = models.TextField()
    prix = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    STATUT_CHOICES = [
        ('validee', 'Validée'),
        ('rejetee', 'Rejetée'),
        ('attente', 'En attente'),
    ]
    statut = models.TextField(choices=STATUT_CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    vendeur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)


    def __str__(self):
        return self.titre