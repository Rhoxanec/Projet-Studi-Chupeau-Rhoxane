from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static 
from website import views
from two_factor.urls import urlpatterns as tf_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    #path("login/", auth_views.LoginView.as_view(template_name="two_factor/login.html"), name="login"),
    path('', include(tf_urls)),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('accueil/', views.accueil, name= 'accueil'),
    path('billetterie/', views.billetterie, name='billetterie'),
    path('moncompte/', views.moncompte, name='moncompte'),
    path('update_mdp', views.update_mdp, name='update_mdp'),
    path('billet/<int:pk>', views.billet, name='billet'),
    path('panier/', include('panier.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

