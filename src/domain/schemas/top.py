# src/domain/schemas/top.py

from pydantic import BaseModel
from typing import List


class TopProcessesResponseSchema(BaseModel):
    top_cpu_processes: List[dict]
    top_memory_processes: List[dict]
