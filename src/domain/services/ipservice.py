"""
Ce module définit une classe de contrôleur pour récupérer les valeurs d'adresse IP.
"""
from fastapi import Request
from domain.models import Ip

class IpService:
    """
    Classe de contrôleur pour les opérations liées aux adresses IP.
    """
    def __init__(self):
        ...

    async def get_ip(self, request: Request) -> Ip:
        """
        Récupère l'adresse IP à partir de la requête.

        Arguments:
            request (Request): Requête contenant les informations de l'adresse IP.

        Returns:
            Ip: Objet représentant l'adresse IP.
        """
        client_host = request.client.host
        return Ip(ip=client_host)
