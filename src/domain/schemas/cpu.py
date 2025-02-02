"""
This module defines a data transfer model for a GetCpuResponseSchema.
"""
from pydantic import BaseModel


class GetCpuResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing CPU information.

    Attributes:
        id (int): The ID of the CPU data.
        usage (str): The CPU usage in string format.
    """

    id: int
    usage: float


class GetCpuCoreResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing CPU core number.

    Attributes:
        number (int): CPU core number.
    """

    number: int

class GetCpuAvgLoadResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing CPU average system load.

    Attributes:
        avgLoad (list[float]): average system load (%).
    """
    avgLoad: list[float]