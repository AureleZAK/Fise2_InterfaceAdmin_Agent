"""
This module defines a data model for Hostname information.
"""
from pydantic import BaseModel

class Hostname(BaseModel):
    """
    Pydantic data model for representing Hostname information.

    Attributes:
        hostname (str): The hostname in string format.
    """
    hostname: str
