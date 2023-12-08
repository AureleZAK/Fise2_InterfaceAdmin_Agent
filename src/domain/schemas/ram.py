"""
This module defines a data transfer model for a GetRamResponseSchema.
"""
from pydantic import BaseModel


class GetRamResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing RAM information.

    Attributes:
        total int: The RAM usage in int format.
        percent float: The Ram usage in float format.
    """
    total : int
    used : int
    free : int
    percent : float
