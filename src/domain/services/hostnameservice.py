"""
This module defines a controller class for fetching RAM values from a monitoring task.
"""
from domain.models import Hostname
from fastapi import Request

class HostService:
    def __init__(self):
        ...

    async def get_hostname(self, request: Request) -> Hostname:

        # Obtenir les données de RAM à partir de monitor_task
        client_hostname = request.client.hostname

        # Créer et retourner un objet Ram avec les données obtenues
        return Hostname(Hostname = client_hostname)