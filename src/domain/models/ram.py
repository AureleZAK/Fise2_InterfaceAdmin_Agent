"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel


# RAM data model
class Ram(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        percent float: The RAM usage in float format.
    """
    percent: float