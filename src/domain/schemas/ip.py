"""
This module defines a data transfer model for a GetIpResponseSchema.
"""
from pydantic import BaseModel

class GetIpResponseSchema(BaseModel):
    """
    Pydantic data model for the response schema representing CPU information.

    Attributes:
        ip (str): the ip 
    """
    ip : str

