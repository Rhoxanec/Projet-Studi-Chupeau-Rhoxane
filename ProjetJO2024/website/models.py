from django.db import models
import datetime


# Utilisateurs
class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mot_de_passe = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.nom} {self.prenom}' 

# Offres
class Offre(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/offre/', blank=True, null=True)

    def __str__(self):
        return self.name 



# Commandes
class Commande(models.Model):
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self):
        return f'{self.offre}' 