"""
Ce module définit une classe de contrôleur pour récupérer les valeurs de la RAM.
"""
from domain.models import Ram
from monitor import MonitorTask

class RamService:
    """
    Classe de contrôleur pour les opérations liées à la RAM.
    """
    def __init__(self):
        ...

    async def get_ram(self, monitor_task: MonitorTask) -> Ram:
        """
        Récupère les valeurs de la RAM depuis une tâche de surveillance.

        Arguments:
            monitor_task (MonitorTask): Tâche de surveillance contenant les informations de la RAM.

        Returns:
            Ram: Objet représentant les informations de la RAM.
        """

        ram_data = monitor_task.ram_stats

        return Ram(
            total=ram_data['total'],
            used=ram_data['used'],
            free=ram_data['free'],
            percent=ram_data['percent']
        )
