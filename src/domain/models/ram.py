"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel

class Ram(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        total (int): The RAM total in int format.
        used (int): The RAM usage in int format.
        free (int): The RAM usage in int format.
        percent (float): The RAM usage in float format.
    """
    def __init__(self, total: int, used: int, free: int, percent: float, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.used = used
        self.free = free
        self.percent = percent
