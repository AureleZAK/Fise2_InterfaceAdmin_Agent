"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel


# RAM data model
class Ram(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        id (int): The ID of the RAM data.
        usage (float): The RAM usage in float format.
    """

    id: int
    usage: float