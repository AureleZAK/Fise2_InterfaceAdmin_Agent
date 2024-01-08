"""
This module defines a data transfer model for a GetCpuResponseSchema.
"""
from pydantic import BaseModel


class GetLogResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing Log information.

    Attributes:
        nbip (int)
        failed (int)
        succeed (int)
        nbwebsites (dict)
    """
    nbip: int
    failed: int
    succeed: int
    nbwebsites: dict

