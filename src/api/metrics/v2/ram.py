"""
This module defines API routes for handling CPU-related data.
"""
from typing import List
from fastapi import APIRouter, Request
from monitor import MonitorTask
from domain.services import RamService
from domain.schemas import (
    ExceptionResponseSchema,
    GetRamResponseSchema
)

ram_router = APIRouter()


@ram_router.get(
    "/usage",
    response_model=GetRamResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def ram_usage(request: Request) -> GetRamResponseSchema:
    """
    Get the percent of used ram

    Args:
        request (Request): The incoming request.

    Returns:
        Percent used
    """
    return await RamService().get_ram(request.app.state.monitortask)

