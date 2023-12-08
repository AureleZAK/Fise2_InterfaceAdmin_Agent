from pydantic import BaseModel

class GetHostnameResponseSchema(BaseModel):
    hostname : str