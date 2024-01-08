"""
Ce module contient les schémas de données pour la gestion des informations système.
"""

from pydantic import BaseModel
from .cpu import GetCpuResponseSchema, GetCpuCoreResponseSchema
from .ram import GetRamResponseSchema
from .ip import GetIpResponseSchema
from .hostname import GetHostnameResponseSchema


class ExceptionResponseSchema(BaseModel):
    """
    Modèle de données Pydantic pour représenter une réponse d'exception.

    Attributs :
        error (str) : Message d'erreur au format chaîne de caractères.
    """
    error: str


__all__ = [
    "GetCpuResponseSchema",
    "GetCpuCoreResponseSchema",
    "GetRamResponseSchema",
    "GetIpResponseSchema",
    "GetHostnameResponseSchema",
    "ExceptionResponseSchema",
]
