"""This module defines a `MonitorTask` class for monitoring metrics on a host."""
import time
import psutil

class MonitorTask:
    """
        A class for monitoring metrics.
    """

    interval: int
    cpu_percent: list[float]
    ram_info: list[float]
    num_cores: int
    ram_stats : dict
    hostname_info : str

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
            ram = psutil.virtual_memory()
            self.ram_stats = {
                'total' : ram.total,
                'used' : ram.used,
                'free' : ram.available,
                'percent' : ram.percent
            }
            time.sleep(self.interval)
            self.ram_info = psutil.virtual_memory()
            self.hostname_info = socket.gethostname()

    def __str__(self) -> str:
        return f"MonitorTask(interval = {self.interval})"
