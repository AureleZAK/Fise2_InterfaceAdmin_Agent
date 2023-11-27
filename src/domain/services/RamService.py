"""
This module defines a controller class for fetching CPU values from a monitoring task.
"""
from typing import List
from domain.models import Cpu
from monitor import MonitorTask


# Controller class to fetch cpu values from monitoring task
class RamService:
    """
    Controller class to fetch RAM values from a monitoring task.
    """

    def __init__(self):
        ...

    async def ram_usage(self, monitor_task: MonitorTask) -> List[Cpu]:
        in enumerate(monitor_task.ram_percent)
        for core, usage in enumerate(monitor_task.cpu_percent):
            cpulist.append(Cpu(id=core, usage=str(usage)))  # Convertir usage en chaîne
        return cpulist

    def __str__(self):
        return self.__class__.__name__
