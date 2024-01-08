"""
Ce fichier contient le schéma de données pour le nom d'hôte.
"""

from pydantic import BaseModel

class GetHostnameResponseSchema(BaseModel):
    """
    Modèle de données Pydantic pour représenter la réponse du nom d'hôte.

    Attributs :
        hostname (str) : Le nom d'hôte au format chaîne de caractères.
    """
    hostname: str
