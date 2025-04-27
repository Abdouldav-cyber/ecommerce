from django.shortcuts import render, get_object_or_404
from .models import Produit, Commande
from django.http import HttpResponseRedirect
from django.urls import reverse

# Afficher la liste des produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/liste.html', {'produits': produits})
  # Changement ici selon ton fichier 'liste.html'

# Afficher les détails d'un produit
def details_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'boutique/product_detail.html', {'produit': produit})  # Changement ici selon ton fichier 'product_detail.html'

# Créer une commande
def creer_commande(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)

    if request.method == "POST":
        quantite = int(request.POST['quantite'])
        nom_client = request.POST['nom_client']
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']
        email = request.POST['email']

        commande = Commande.objects.create(
            produit=produit,
            quantite=quantite,
            nom_client=nom_client,
            adresse=adresse,
            telephone=telephone,
            email=email
        )

        # Rediriger après la commande
        return HttpResponseRedirect(reverse('commande_confirmation', args=[commande.id]))

    return render(request, 'passer_commande.html', {'produit': produit})  # Changement ici selon ton fichier 'passer_commande.html'

# Confirmer la commande
def commande_confirmation(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    return render(request, 'boutique/order_confirmation.html', {'commande': commande})  # Changement ici selon ton fichier 'order_confirmation.html'
