"""
Ce module définit une classe de contrôleur pour récupérer les valeurs du CPU.
"""
from typing import List
from domain.models import Cpu
from monitor import MonitorTask


# Controller class to fetch cpu values from monitoring task
class CpuService:
    """
    Classe de contrôleur pour les opérations liées au CPU.
    """

    def __init__(self):
        ...

    async def get_cpu(self, monitor_task: MonitorTask) -> List[Cpu]:
        """
        Récupère les valeurs du CPU depuis une tâche de surveillance.

        Arguments:
            monitor_task (MonitorTask): Tâche de surveillance contenant les informations du CPU.

        Returns:
            List[Cpu]: Liste d'objets représentant les valeurs du CPU.
        """

        cpulist = []
        for core, usage in enumerate(monitor_task.cpu_percent):
            cpulist.append(Cpu(id=core, usage=usage))  # Convertir usage en chaîne
        return cpulist

    def __str__(self):
        return self.__class__.__name__
