from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .form import CustomUserCreationForm, UpdateUserForm, ChangePasswordForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Offre
from django_otp.plugins.otp_totp.models import TOTPDevice
#from .forms import Enable2FAForm

# Create your views here.

def update_mdp(request):
    if request.user.is_authenticated:
        current_user = request.user 
        # Si l'utilisateur remplie le formulaire
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            # On vérifie si le formulaire est valide
            if form.is_valid():
                form.save()
                messages.success(request, "Votre mot de passe a été mis à jour, merci de vous reconnecter")
                login(request, current_user)
                return redirect('connexion')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect('update_mdp')
        else:
            form = ChangePasswordForm(current_user)
            return render(request, "update_mdp.html", {'form':form})
    else:
        messages.success(request, "Vous devez être connecté pour voir cette page")
        return redirect('accueil')

def accueil(request):
    return render(request, 'accueil.html')

def billetterie(request):
    offres = Offre.objects.all()
    return render(request, 'billetterie.html', {'offres': offres})

def billet(request,pk):
    billet = Offre.objects.get(id=pk)
    return render(request, 'billet.html', {'billet': billet})

def moncompte(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login(request, current_user)
            messages.success(request, "Utilisateur mis à jour")
            return redirect('accueil')
        return render(request, 'moncompte.html', {'user_form':user_form})
    else:
        messages.success(request, "Vous devez être connecté pour accéder à cette page")
        return redirect('accueil')
  

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
    return redirect('accueil')

def deconnexion(request):
    logout(request)
    return render(request, 'accueil.html')


