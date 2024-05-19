from django.shortcuts import render, get_object_or_404
from .panier import Panier
from website.models import Offre
from django.http import JsonResponse

# Create your views here.

def panier_summary(request):
    panier = Panier(request)
    panier_offres = panier.get_offres
    return render(request, 'panier_summary.html', {"panier_offres":panier_offres})

def panier_add(request):
    panier = Panier(request)
    if request.POST.get('action')=='post':
        offre_id = int(request.POST.get('offre_id'))
        offre = get_object_or_404(Offre, id=offre_id)
        panier.add(offre=offre)
        # Obtenir la quantité du panier
        panier_quantity = panier.__len__()

        # Renvoie la réponse 
        # response = JsonResponse({'offre nom: ': offre.name})
        response = JsonResponse({'qty':panier_quantity})
        return response

def panier_delete(request):
    return render(request, 'panier_delete.html', {})

def panier_update(request):
    return render(request, 'panier_update.html', {})