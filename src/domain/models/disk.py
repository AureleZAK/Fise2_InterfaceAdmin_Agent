"""
This module defines a data model for Disk information.
"""
from pydantic import BaseModel


# CPU data model
class Disk(BaseModel):
    """
    Pydantic data model for representing Disk information.

    Attributes:
        total (float): The total space expressed in bytes 
        used (float): The used space expressed in bytes 
        percent (float): The percentage usage
    """
    total: float
    used: float
    percent: float

