"""
This module defines a data model for RAM information.
"""
from pydantic import BaseModel


# CPU data model
class Ip(BaseModel):
    
    ip: str