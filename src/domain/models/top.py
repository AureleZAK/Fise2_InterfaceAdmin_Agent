# src/domain/models/top.py

from pydantic import BaseModel
from typing import List

class TopProcessModel(BaseModel):
    pid: int
    name: str
    cpu_percent: float
    memory_percent: float
