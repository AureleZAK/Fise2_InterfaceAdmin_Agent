"""
Ce module définit une classe de contrôleur pour récupérer les valeurs du nom d'hôte.
"""
from domain.models import Hostname
from monitor import MonitorTask

class HostService:
    """
    Classe de contrôleur pour les opérations liées au nom d'hôte.
    """
    def __init__(self):
        ...

    async def get_hostname(self, monitor_task: MonitorTask) -> Hostname:
        """
        Récupère le nom d'hôte à partir d'une tâche de surveillance.

        Arguments:
            monitor_task (MonitorTask): Tâche de surveillance contenant le nom d'hôte.

        Returns:
            Hostname: Objet représentant le nom d'hôte.
        """

        client_hostname = monitor_task.hostname_info

        return Hostname(hostname=client_hostname)
