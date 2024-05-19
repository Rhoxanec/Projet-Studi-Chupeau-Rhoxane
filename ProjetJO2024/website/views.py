from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .form import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Offre

# Create your views here.

def accueil(request):
    return render(request, 'accueil.html')

def billetterie(request):
    offres = Offre.objects.all()
    return render(request, 'billetterie.html', {'offres': offres})

def billet(request,pk):
    billet = Offre.objects.get(id=pk)
    return render(request, 'billet.html', {'billet': billet})

def moncompte(request):
    return render(request, 'moncompte.html')

#def panier(request):
#    return render(request, 'panier.html')

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
#def panier(request):
#return render(request, 'panier.html')

def deconnexion(request):
    logout(request)
    return render(request, 'accueil.html')


