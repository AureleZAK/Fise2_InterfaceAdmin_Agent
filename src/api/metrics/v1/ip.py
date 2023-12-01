"""
This module defines API routes for handling RAM-related data.
"""
from typing import List
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetIpResponseSchema,
)
from domain.services import RamService

ip_router = APIRouter()


@ip_router.get(
    "/ip",
    response_model=GetIpResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_ip(request: Request) -> GetIpResponseSchema:
    """
    Route to get the number of CPU core.

    Args:
        request (Request): The incoming request.

    Returns:
        int: number of cpu core.
    """
    client_ip = request.client.host

    return {"Client IP": client_ip}

    
 
