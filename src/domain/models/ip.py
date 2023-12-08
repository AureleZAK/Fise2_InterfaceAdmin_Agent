"""
This module defines a data model for IP information.
"""
from pydantic import BaseModel


# CPU data model
class Ip(BaseModel):
    """
    Pydantic data model for representing RAM information.

    Attributes:
        ip (str): the ip in string format.

    """
    ip: str