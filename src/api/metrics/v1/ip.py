"""
This module defines API routes for handling RAM-related data.
"""
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetIpResponseSchema,
)
from domain.services import IpService

ip_router = APIRouter()


@ip_router.get(
    "/ip",
    response_model=GetIpResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_ip(request: Request):
    """
    Route to get the number of CPU core.

    Args:
        request (Request): The incoming request.

    Returns:
        int: number of cpu core.
    """
    ip_data = await ip_service.get_ip(request)

    return ip_data

    
 
