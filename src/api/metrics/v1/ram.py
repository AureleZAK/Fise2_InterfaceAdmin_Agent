"""
This module defines API routes for handling RAM-related data.
"""
from typing import List
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetRamResponseSchema,
)
from domain.services import RamService

ram_router = APIRouter()


@ram_router.get(
    "/ram",
    response_model=GetRamResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_core_number(request: Request) -> GetRamResponseSchema:
    """
    Route to get the number of CPU core.

    Args:
        request (Request): The incoming request.

    Returns:
        int: number of cpu core.
    """
    return GetRamResponseSchema(number=request.app.state.monitortask.num_cores)
