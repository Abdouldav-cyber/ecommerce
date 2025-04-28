from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0002_produit_stock'),  # <-- remplace par ton vrai dernier fichier de migration
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='prix_total',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
    ]
