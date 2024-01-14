# src/domain/schemas/top.py

from pydantic import BaseModel
from typing import List

class TopProcessModel(BaseModel):
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float

class TopProcessesResponseSchema(BaseModel):
    top_cpu_processes: List[TopProcessModel]
    top_memory_processes: List[TopProcessModel]
