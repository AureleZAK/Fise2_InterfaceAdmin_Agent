# src/domain/services/topservice.py

from fastapi import HTTPException
from domain.schemas.top import TopProcessesResponseSchema
from monitor import MonitorTask  # Importez localement


class TopProcessesService:

    def __init__(self):
        ...

    async def get_top_processes(self, monitor_task: MonitorTask) -> TopProcessesResponseSchema:
        try:
            
            # Utilisez la classe MonitorTask pour récupérer les informations nécessaires
            top_stats = monitor_task.top_stats
            # Ajoutez votre logique pour obtenir les processus les plus consommateurs
            top_cpu_processes = top_stats['top_cpu_processes']
            top_memory_processes = top_stats['top_memory_processes']

            return TopProcessesResponseSchema(
                top_cpu_processes=top_cpu_processes,
                top_memory_processes=top_memory_processes,
            )
        except Exception as e:
            print(f"Error in get_top_processes: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))
