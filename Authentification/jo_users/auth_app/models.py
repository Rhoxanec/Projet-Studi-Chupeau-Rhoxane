from django.db import models

class Utilisateurs(models.Model):
    nom = models.CharField(max_length=50)
    #prenom = models.CharField(max_length=50)
    #email = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)