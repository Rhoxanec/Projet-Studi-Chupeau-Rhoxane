from django.shortcuts import render, get_object_or_404
from .panier import Panier
from website.models import Offre
from django.http import JsonResponse

# Create your views here.

def panier_summary(request):
    panier = Panier(request)
    panier_offres = panier.get_offres()
    quantities = panier.get_quantity()
    totals = panier.total()
    return render(request, 'panier_summary.html', {"panier_offres":panier_offres, 'quantities':quantities, "totals":totals})


def panier_add(request):
    panier = Panier(request)
    if request.POST.get('action')=='post':
        offre_id = int(request.POST.get('offre_id'))
        offreqty = int(request.POST.get('billetqty'))

        offre = get_object_or_404(Offre, id=offre_id)
        panier.add(offre=offre, offreqty=offreqty)
        # Obtenir la quantité du panier
        panier_quantity = panier.__len__()

        # Renvoie la réponse 
        # response = JsonResponse({'offre nom: ': offre.name})
        response = JsonResponse({"qty": panier.__len__() })
        return response

def panier_delete(request):
    panier = Panier(request)
    if request.POST.get('action')=='post':
        offre_id = int(request.POST.get('offre_id'))

        panier.delete(offre=offre_id)
        response = JsonResponse({"offre": offre_id})
        return response

def panier_update(request):
    panier = Panier(request)
    if request.POST.get('action')=='post':
        offre_id = int(request.POST.get('offre_id'))
        offreqty = int(request.POST.get('billetqty'))

        panier.update(offre=offre_id, quantity=offreqty)

        # Renvoie la réponse 
        # response = JsonResponse({'offre nom: ': offre.name})
        response = JsonResponse({"qty": offreqty})
        return response
