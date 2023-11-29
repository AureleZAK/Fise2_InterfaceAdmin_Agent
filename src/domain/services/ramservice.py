"""
This module defines a controller class for fetching CPU values from a monitoring task.
"""
from typing import List
from domain.models import Ram
from monitor import MonitorTask


# Controller class to fetch cpu values from monitoring task
class RamService:
    """
    Controller class to fetch CPU values from a monitoring task.
    """

    def __init__(self):
        ...

    async def get_ram(self, monitor_task: MonitorTask) -> Ram:
        ram =Ram()
        for total, percent in enumerate(monitor_task.ram_percent):
            ram.total = total
            ram.percent =percent
        return ram

    def __str__(self):
        return self.__class__.__name__
