from pydantic import BaseModel


class GetIpResponseSchema(BaseModel):
    ip : str