from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static 
from website import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('inscription/', views.inscription, name='inscription'),
    path('accueil/', views.accueil, name= 'accueil'),
    path('billetterie/', views.billetterie, name='billetterie'),
    path('moncompte/', views.moncompte, name='moncompte'),
    path('update_mdp', views.update_mdp, name='update_mdp'),
    path('billet/<int:pk>', views.billet, name='billet'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('panier/', include('panier.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

