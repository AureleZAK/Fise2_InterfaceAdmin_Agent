"""This module defines a `MonitorTask` class for monitoring metrics on a host."""
import time
import psutil
import socket


class MonitorTask:
    """
        A class for monitoring metrics.
    """

    interval: int
    cpu_percent: list[float]
    cpu_frequency = float
    cpu_avg_load_percentage: list[float]
    ram_info: list[float]
    num_cores: int
    ram_stats : dict
    hostname_info : str
    disk_stats: dict

    def __init__(self) -> None:
        """
        Initialize the MonitorTask class.

        Add initialization tasks here like checks
        The monitoring interval is 3 seconds.
        """
        self.interval = 3
        self.num_cores = psutil.cpu_count(logical=False)
        self.ram_stats = {}

    def monitor(self):
        """Continuously monitor and store the result in an attribute."""
        while True:
            self.cpu_percent = psutil.cpu_percent(percpu=True)
            self.cpu_frequency = psutil.cpu_freq().current
            self.cpu_avg_load_percentage = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
            ram = psutil.virtual_memory()
            self.ram_stats = {
                'total' : ram.total,
                'used' : ram.used,
                'free' : ram.available,
                'percent' : ram.percent
            }
            self.ram_info = psutil.virtual_memory()
            self.hostname_info = socket.gethostname()
            disk = psutil.disk_usage('/')
            self.disk_stats = {
                'total': disk.total,
                'used': disk.used,
                'percent': disk.percent
            }
            time.sleep(self.interval)           

    def __str__(self) -> str:
        return f"MonitorTask(interval = {self.interval})"
