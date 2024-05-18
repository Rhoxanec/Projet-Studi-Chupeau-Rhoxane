class Panier():
    def __init__(self, request):
        self.session = request.session 

        # On récupère la clé sur la session actuelle si elle existe 
        panier = self.session.get('session_key')

        # S'il y a un nouvel utilisateur qui n'a pas de clé, créé en une 
        if 'session.key' not in request.session:
            panier = self.session['session_key'] = {}

        # S'assurer que le panier est disponible sur toutes les pages
        self.panier = panier 

    def add(self, offre):
        offre_id = str(offre.id)
        if offre_id in self.panier: 
            pass
        else: 
            self.panier [offre_id] = {'price': str(offre.price)}
        self.session.modified = True