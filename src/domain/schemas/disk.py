from pydantic import BaseModel

class GetDiskResponseSchema(BaseModel):
    total: float
    used: float
    percent: float
