"""
This module defines a data transfer model for a GetRamResponseSchema.
"""
from pydantic import BaseModel


class GetRamResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing RAM information.

    Attributes:
        total (int): The RAM total in int format.
        used (int): The RAM usage in int format.
        free (int): The RAM usage in int format.
        percent (float): The RAM usage in float format.
    """
    total : int
    used : int
    free : int
    percent : float
