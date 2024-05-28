from django.test import TestCase
from .models import Offre, Utilisateur, UserProfile 
from panier.panier import Panier

# Create your tests here.
class OffreTestCase(TestCase):
    def setUp(self):
        Offre.objects.create(name='TEST', price='10', description='Offre de test', image='')
        self.panier = Panier
        
    def test_ajout_offre_panier(self):
         # Je vérifie que mon offre a été créée
        offretest = Offre.objects.get(name='TEST')
        self.assertEqual(offretest.name, 'TEST')
        self.assertEqual(offretest.price, 10)
        self.assertEqual(offretest.description, 'Offre de test')
        self.assertEqual(offretest.image, '')


class UtilisateurTestCase(TestCase):
    def setUp(self):
        Utilisateur.objects.create(nom='Jean', prenom='Paul', email='test@email.com', mot_de_passe='Test@1234')
        self.utilisateur = Utilisateur
        
    def test_ajout_creation_utilisateur(self):
         # Je vérifie que mon utilisateur a été créé
        utilisateurtest = Utilisateur.objects.get(nom='Jean')
        self.assertEqual(utilisateurtest.nom, 'Jean')
        self.assertEqual(utilisateurtest.prenom, 'Paul')
        self.assertEqual(utilisateurtest.email, 'test@email.com')
        self.assertEqual(utilisateurtest.mot_de_passe, 'Test@1234')


       
