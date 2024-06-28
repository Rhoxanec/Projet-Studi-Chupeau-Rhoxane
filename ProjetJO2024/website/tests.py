from django.test import TestCase
from .models import Offre, Utilisateur, UserProfile, Commande
from panier.panier import Panier
from unittest.mock import patch 

# Create your tests here.
class TestCaseOffre(TestCase):
    def setUp(self):
        # Création de l'offre "prenium"
        Offre.objects.create(name='prenium', price='10', description='Offre de test', image='')
        Offre.objects.create(name='duo', price='15', description='Offre de test2', image='')
        self.offre = Offre.objects.create(name='duo', price='15', description='Offre de test2', image='')
             
    def test_creation_offre(self):
         # Je vérifie que l'offre est créée
        offreprenium = Offre.objects.get(name='prenium')
        offreduo = Offre.objects.get(name='duo')
        #self.panier = Panier.add(self, offreduo, 1)
        self.assertEqual(offreduo.name, self.offre.name)
        self.assertEqual(offreduo.price, self.offre.price )
        self.assertEqual(offreduo.description, self.offre.description)
        self.assertEqual(offreduo.image, '')



class TestCaseUtilisateurCommande(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur.objects.create(nom='Jean', prenom='Paul', email='test@email.com', mot_de_passe='Test@1234')
        #self.profile = UserProfile.objects.create(Utilisateur)
       # UserProfile.objects.create()
        Offre.objects.create(name='prenium', price='10', description='Offre de test', image='')
        offreprenium = Offre.objects.get(name='prenium')
        self.commande = Commande.objects.create(offre= offreprenium, utilisateur= self.utilisateur, nom='Jean', prenom='Paul', quantity= 2)
        Offre.objects.create(name='trio', price='15', description='Offre de test3', image='')
        offretrio = Offre.objects.get(name='trio')
        self.commande.offre = offretrio
        

    def test_ajout_creation_utilisateur(self):
         # Je vérifie que mon utilisateur a été créé
        utilisateurtest = Utilisateur.objects.get(nom='Jean')
        self.assertEqual(utilisateurtest.nom, self.utilisateur.nom)
        self.assertEqual(utilisateurtest.prenom, self.utilisateur.prenom)
        self.assertEqual(utilisateurtest.email, self.utilisateur.email)
        self.assertEqual(utilisateurtest.mot_de_passe, self.utilisateur.mot_de_passe)

    def test_modification_commande_existante(self):
         # Je vérifie la modification d'une commande existante
        commandetest = Commande.objects.get(nom='trio')
        self.assertEqual(commandetest.offre, self.commande.offre)
        self.assertEqual(commandetest.utilisateur, self.commande.utilisateur)
        self.assertEqual(commandetest.nom, self.commande.nom)
        self.assertEqual(commandetest.prenom, self.commande.prenom)
        self.assertEqual(commandetest.quantity, self.commande.quantity)


       
