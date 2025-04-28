from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Champ ajouté pour le stock
    image = models.ImageField(upload_to='produits/')

    def __str__(self):
        return self.nom

class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    nom_client = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Champ ajouté
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.nom_client} - {self.produit.nom}"
