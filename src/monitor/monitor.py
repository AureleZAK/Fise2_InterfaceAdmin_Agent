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
    cpu_avg_load_percentage: list[float]
    ram_info: list[float]
    num_cores: int
    ram_stats : dict
    hostname_info : str
    disk_stats: dict
    top_stats: dict 

    def __init__(self) -> None:
        """
        Initialize the MonitorTask class.

        Add initialization tasks here like checks
        The monitoring interval is 3 seconds.
        """
        self.interval = 3
        self.num_cores = psutil.cpu_count(logical=False)
        self.ram_stats = {}
        self.top_stats = {} # Ajoutez ceci pour créer une instance du service
  
  


    def monitor(self):
        """Continuously monitor and store the result in an attribute."""
        while True:
            self.cpu_percent = psutil.cpu_percent(percpu=True)
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
        

            top_cpu_processes = []
            for proc in sorted(psutil.process_iter(), key=lambda x: x.cpu_percent(), reverse=True)[:6]:
                top_cpu_processes.append({
                    'pid': proc.pid,
                    'name': proc.name(),
                    'cpu_percent': proc.cpu_percent(),
                })

            # Obtenez les processus mémoire
            top_memory_processes = []
            for proc in sorted(psutil.process_iter(), key=lambda x: x.memory_info().rss, reverse=True)[:5]:
                top_memory_processes.append({
                    'pid': proc.pid,
                    'name': proc.name(),
                    'memory_usage': proc.memory_info().rss,
                })
                filtered_top_cpu_processes = [process for process in top_cpu_processes if process["name"] != "System Idle Process"]
                sorted_filtered_top_cpu_processes = sorted(filtered_top_cpu_processes, key=lambda x: x['cpu_percent'], reverse=True)

                self.top_stats = {
                    'top_cpu_processes': sorted_filtered_top_cpu_processes,
                    'top_memory_processes': top_memory_processes,
}

            time.sleep(self.interval)

    def __str__(self) -> str:
        return f"MonitorTask(interval = {self.interval})"
