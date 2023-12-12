"""
This module defines a controller class for fetching RAM values from a monitoring task.
"""
from domain.models import Hostname
from fastapi import Request
from monitor import MonitorTask

class HostService:
    def __init__(self):
        ...

    async def get_hostname(self, monitor_task: MonitorTask) -> Hostname:

        # Obtenir les données de hostname à partir de monitor_task
        client_hostname = monitor_task.hostname_info

        # Créer et retourner un objet Ram avec les données obtenues
        return Hostname(Hostname = client_hostname)