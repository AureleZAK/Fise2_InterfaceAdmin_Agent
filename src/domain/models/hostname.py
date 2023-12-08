"""
This module defines a data model for Hostname information.
"""
from pydantic import BaseModel
#tstsd

# Hostname data model
class Hostname(BaseModel):
    
    hostname : str