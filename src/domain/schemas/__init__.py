from pydantic import BaseModel
from .cpu import GetCpuResponseSchema, GetCpuCoreResponseSchema
from .ram import GetRamResponseSchema
from .ip import GetIpResponseSchema
from .hostname import GetHostnameResponseSchema
from .log import GetLogResponseSchema


class ExceptionResponseSchema(BaseModel):
    error: str


__all__ = [
    "GetCpuResponseSchema",
    "GetCpuCoreResponseSchema",
    "GetRamResponseSchema",
    "GetIpResponseSchema",
    "GetHostnameResponseSchema",
    "ExceptionResponseSchema",
    "GetLogResponseSchema",
]
