"""
This module defines a data model for CPU information.
"""
from pydantic import BaseModel


# CPU data model
class Log(BaseModel):
    """
    Pydantic data model for representing Log information.

    Attributes:
        nbip (int)
        failed (int)
        succed (int)
        nbwebsites (dict)
    """
    nbip: int
    failed: int
    succeed: int
    nbwebsites: dict
