from django.shortcuts import render

# Create your views here.

def panier_summary(request):
    return render(request, 'panier_summary.html', {})

def panier_add(request):
    return render(request, 'panier_summary.html', {})

def panier_delete(request):
    return render(request, 'panier_summary.html', {})

def panier_update(request):
    return render(request, 'panier_summary.html', {})