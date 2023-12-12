"""
This module defines a controller class for fetching RAM values from a monitoring task.
"""
from domain.models import Ip
from fastapi import Request

class IpService:
    """
    Controller class to fetch IP values from a monitoring task.
    """
    def __init__(self):
        ...

    async def get_ip(self, request: Request) -> Ip:

        client_host = request.client.host
        return Ip(ip = client_host)