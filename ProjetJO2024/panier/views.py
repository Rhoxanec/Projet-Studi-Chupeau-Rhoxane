from django.shortcuts import render, get_object_or_404
from .panier import Panier
from website.models import Offre
from django.http import JsonResponse

# Create your views here.

def panier_summary(request):
    return render(request, 'panier_summary.html', {})

def panier_add(request):
    panier = Panier(request)
    if request.POST.get('action')=='post':
        offre_id = int(request.POST.get('offre_id'))
        offre = get_object_or_404(Offre, id=offre_id)
        panier.add(offre=offre)
        response = JsonResponse({'offre nom: ': offre.name})

        return response

def panier_delete(request):
    return render(request, 'panier_delete.html', {})

def panier_update(request):
    return render(request, 'panier_update.html', {})