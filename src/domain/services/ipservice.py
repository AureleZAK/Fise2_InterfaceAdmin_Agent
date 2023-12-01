"""
This module defines a controller class for fetching RAM values from a monitoring task.
"""
from domain.models import Ip
from monitor import MonitorTask

class IpService:
    def __init__(self):
        ...

    async def get_ip(self, monitor_task: MonitorTask) -> Ip:

        # Obtenir les données de RAM à partir de monitor_task
        client_host = request.client.host

        # Créer et retourner un objet Ram avec les données obtenues
        return Ip(ip= client_host)