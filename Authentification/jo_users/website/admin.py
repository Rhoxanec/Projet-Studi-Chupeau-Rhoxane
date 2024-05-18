from django.contrib import admin
from .models import Utilisateur, Offre, Commande

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Offre)
admin.site.register(Commande)