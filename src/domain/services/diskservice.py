"""
Ce module définit une classe de contrôleur pour récupérer les valeurs de la RAM.
"""
from domain.models import Disk
from monitor import MonitorTask

class DiskService:
    """
    Classe de contrôleur pour les opérations liées à la RAM.
    """
    def __init__(self):
        ...

    async def get_disk(self, monitor_task: MonitorTask) -> Disk:
        """
        Récupère les valeurs du Disk depuis une tâche de surveillance.

        Arguments:
            monitor_task (MonitorTask): Tâche de surveillance contenant les informations du Disk

        Returns:
            Disk: Objet représentant les informations du Disk.
        """

        disk_data = monitor_task.disk_stats

        return Disk(
            total=disk_data['total'],
            used=disk_data['used'],
            percent=disk_data['percent']
        )