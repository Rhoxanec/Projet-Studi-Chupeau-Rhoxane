from website.models import Offre

class Panier():
    def __init__(self, request):
        self.session = request.session

        # On récupère la clé sur la session actuelle si elle existe 
        panier = self.session.get('session_key')

        # S'il y a un nouvel utilisateur qui n'a pas de clé, créé en une 
        if 'session_key' not in request.session:
            panier = self.session['session_key'] = {}

        # S'assurer que le panier est disponible sur toutes les pages
        self.panier = panier


    def add(self, offre, offreqty):
        offre_id = str(offre.id)
        if offre_id in self.panier:
            self.panier[offre_id] += int(offreqty)
        else:
            self.panier[offre_id] = int(offreqty)
        self.session.modified = True

    def __len__(self):
        return sum(item for item in self.panier.values())
    
    def get_offres(self):
        offre_ids = self.panier.keys()
        offres = Offre.objects.filter(id__in=offre_ids)
        return offres
    
    def get_quantity(self):
        quantities = self.panier
        return quantities
    
    def update(self, offre, quantity):
        offre_id = str(offre)
        offre_qty = int(quantity)

        # Récupérer le panier
        notrepanier = self.panier
        # Mettre à jour le panier
        notrepanier[offre_id] = offre_qty

        self.session.modified = True 

        thing = self.panier
        return thing
