from pydantic import BaseModel
from .cpu import GetCpuResponseSchema, GetCpuCoreResponseSchema
from .ram import GetRamResponseSchema
from .ip import GetIpResponseSchema


class ExceptionResponseSchema(BaseModel):
    error: str


__all__ = [
    "GetCpuResponseSchema",
    "GetCpuCoreResponseSchema",
    "GetRamResponseSchema"
    "GetIpResponseSchema"
    "ExceptionResponseSchema",
]
