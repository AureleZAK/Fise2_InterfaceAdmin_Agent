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

        ram = Ram(total= monitor_task.ram_info.total , percent= monitor_task.ram_info.percent)
        return ram

    def __str__(self):
        return self.__class__.__name__
