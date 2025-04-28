from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('boutique', '0003_ajout_prix_total'),  # remplace par ton dernier fichier
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='date_commande',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
