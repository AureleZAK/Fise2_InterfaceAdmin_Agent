from pydantic import BaseModel


class GetRamResponseSchema(BaseModel):
    total : int
    used : int
    free : int
    percent : float