from django.shortcuts import render, redirect, get_object_or_404
from .panier import Panier
from website.models import Offre, Commande
from django.http import JsonResponse
from io import BytesIO
from ecomjo import settings
from django.contrib.auth.models import User
from django.contrib import messages
import base64
import secrets 
import qrcode
import datetime


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
    
def e_ticket(request):
    panier = Panier(request)
    panier_offres = panier.get_offres()   
    quantities = panier.get_quantity()
    #Commande.utilisateur = current_user
    #Commande.quantity = quantities
    totals = panier.total()
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
    # Génération du qrcode
        username = current_user.username
        dt = f'{datetime.datetime.now():%Y%m%d}'
        qrcodeimg = secrets.token_urlsafe(10)
        for offre in panier_offres: 
            qrcodeimg = qrcodeimg + username + dt + offre.name
            image = qrcode.make(qrcodeimg)
            #Commande.offre = offre
    #votre_ticket = BytesIO()
            votre_ticket = f'votre_ticket.png'
            image.save(settings.MEDIA_ROOT + '/' + offre.name + votre_ticket)
            

        ticket_data = {
            'ticket_id': qrcodeimg,
            'user_nom': username,
            #'user_prenom': 'Le prenom de l utilisateur',
            'panier_offres': panier_offres,
            'qty': quantities,
            'totals': totals,
            'qrcode': votre_ticket,

         }

        return render(request, 'e_ticket_summary.html', {'ticket_data': ticket_data})
    return render(request, 'panier_summary.html', {"panier_offres":panier_offres, 'quantities':quantities, "totals":totals})
    
                               
