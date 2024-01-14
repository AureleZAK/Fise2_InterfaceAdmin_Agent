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
        print(request)
        if request.client:
            client_host = request.client.host
        # Rest of the code
        else:
        # Handle the case when request.client is None
            print("Client information not available.")
            client_host = "unknown"  # or any default value you want to set

        return Ip(ip=client_host)