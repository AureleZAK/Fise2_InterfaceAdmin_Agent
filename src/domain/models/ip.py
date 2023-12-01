"""
This module defines a data model for IP information.
"""
from pydantic import BaseModel


# CPU data model
class Ip(BaseModel):
    
    def __init__(self, ip: str):
            self.ip = ip
            