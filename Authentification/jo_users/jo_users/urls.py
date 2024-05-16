from django.contrib import admin
from django.urls import path
from auth_app import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('', views.inscription, name='inscription'),
    path('accueil/', views.accueil, name= 'accueil'),
    path('billetterie/', views.billetterie, name='billetterie'),
    path('moncompte/', views.moncompte, name='moncompte'),
    path('panier/', views.panier, name='panier'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]
