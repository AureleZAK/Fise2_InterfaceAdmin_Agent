# models.py dans votre application "dashboard"
from django.db import models

class ServerData(models.Model):
    # Vos champs de modèle vont ici
    champ1 = models.CharField(max_length=100)
    champ2 = models.IntegerField()
    # Ajoutez plus de champs au besoin

    def __str__(self):
        return f"{self.champ1} - {self.champ2}"  # Ajustez ceci en fonction de la structure de votre modèle
