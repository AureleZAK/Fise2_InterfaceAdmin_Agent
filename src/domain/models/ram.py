"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel


# CPU data model
class Ram(BaseModel):
    
    def __init__(self, total: int, used: int, free: int, percent: float):
            self.total = total
            self.used = used
            self.free = free
            self.percent = percent