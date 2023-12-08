"""
This module defines a data model for Hostname information.
"""
from pydantic import BaseModel


# Hostname data model
class Hostname(BaseModel):
    
    hostname : str