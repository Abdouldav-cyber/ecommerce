from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),  # Liste des produits (accueil)
    path('produit/<int:produit_id>/', views.details_produit, name='details_produit'),  # Détails d'un produit
    path('produit/<int:produit_id>/commande/', views.creer_commande, name='creer_commande'),  # Passer une commande
    path('commande/<int:commande_id>/confirmation/', views.commande_confirmation, name='commande_confirmation'),  # Confirmation de commande
]
