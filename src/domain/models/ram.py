"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel


# RAM data model
class Ram(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        total int: The RAM usage in int format.
        percent float: The RAM usage in float format.
    """
    total: int
    percent: float