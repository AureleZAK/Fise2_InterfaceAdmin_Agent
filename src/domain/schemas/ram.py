from pydantic import BaseModel


class getRamResponseSchema(BaseModel):
    total : int
    used : int
    free : int
    percent : float