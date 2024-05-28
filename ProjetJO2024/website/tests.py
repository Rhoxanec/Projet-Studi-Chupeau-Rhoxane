from django.test import TestCase
from .models import Offre
from panier.panier import Panier

# Create your tests here.
class OffreTestCase(TestCase):
    def setUp(self):
        #Panier(self)
        Offre.objects.create(name='TEST', price='10', description='Offre de test', image='')
        #panier = self.session['session_key'] = {}
        self.panier = Panier
        
    
    

    def test_ajout_offre_panier(self):
         # Je vérifie que mon offre a été créée
        offretest = Offre.objects.get(name='TEST')
        #Panier.add(self, offre= offretest, offreqty= 1) 
        #test_qty= self.panier.__getitem__()
        self.assertEqual(offretest.name, 'TEST')
        self.assertEqual(offretest.price, 10)
         # Je vérifie l'ajout de l'offre à mon panier 



#def add(self, offre, offreqty):
       # offre_id = str(offre.id)
       # if offre_id in self.panier:
       #     self.panier[offre_id] += int(offreqty)
        #else:
        #    self.panier[offre_id] = int(offreqty)
       # self.session.modified = True

#self.data = {
    #self.user = User.objects.create_user(**self.data)

#def test_profile(self):
    #self.assertEqual(self.profile.user, self.user)