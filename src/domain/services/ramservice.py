"""
This module defines a controller class for fetching RAM values from a monitoring task.
"""
from domain.models import Ram
from monitor import MonitorTask

class RamService:
    """
    Controller class to fetch RAM values from a monitoring task.
    """
    def __init__(self):
        ...

    async def get_ram(self, monitor_task: MonitorTask) -> Ram:

        ram_data = monitor_task.ram_stats

        return Ram(
            total=ram_data['total'],
            used=ram_data['used'],
            free=ram_data['free'],
            percent=ram_data['percent']
        )