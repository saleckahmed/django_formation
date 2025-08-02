from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ( 'CLIENT', 'client'),
        ('ADMIN', 'admin')
    ]
    role = models.CharField(max_length=6, choices=ROLE_CHOICES, default='CLIENT')
    telephone = models.IntegerField()

class Meta:
    models =  Utilisateur
    fields = ['username', 'password', 'role']

