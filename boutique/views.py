from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Commande
from django.http import HttpResponseRedirect
from django.urls import reverse

# Afficher la liste des produits
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'boutique/liste.html', {'produits': produits})

# Afficher les détails d'un produit
def details_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'boutique/product_detail.html', {'produit': produit})

# Créer une commande
def creer_commande(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)

    if request.method == 'POST':
        nom_client = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        quantite = int(request.POST.get('quantite', 0))  # Utiliser une valeur par défaut si vide

        # Vérifier que tous les champs obligatoires sont remplis
        if not nom_client or not adresse or not email or not telephone or quantite <= 0:
            return render(request, 'boutique/passer_commande.html', {
                'produit': produit,
                'error': "Tous les champs sont obligatoires et la quantité doit être positive.",
            })

        if quantite > produit.stock:
            # Stock insuffisant
            return render(request, 'boutique/passer_commande.html', {
                'produit': produit,
                'error': "Stock insuffisant pour la quantité demandée.",
            })

        # Création de la commande
        commande = Commande.objects.create(
            produit=produit,
            quantite=quantite,
            nom_client=nom_client,
            adresse=adresse,
            email=email,
            telephone=telephone,
            prix_total=quantite * produit.prix
        )

        # Mise à jour du stock
        produit.stock -= quantite
        produit.save()

        # Rediriger vers une page de confirmation pour éviter de re-soumettre le formulaire
        return HttpResponseRedirect(reverse('commande_confirmation', args=[commande.id]))

    return render(request, 'boutique/passer_commande.html', {'produit': produit})

# Confirmer la commande
def commande_confirmation(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    return render(request, 'boutique/order_confirmation.html', {'commande': commande})
