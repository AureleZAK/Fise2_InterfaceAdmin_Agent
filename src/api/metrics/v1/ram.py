"""
This module defines API routes for handling RAM-related data.
"""
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetRamResponseSchema,
)

ram_router = APIRouter()


@ram_router.get(
    "",
    response_model=GetRamResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_ram(request: Request) -> GetRamResponseSchema:
    """
    Route to get informations regarding the ram.

    Args:
        request (Request): The incoming request.

    Returns:
        Ram: ram informations.
    """
    ram_stats = request.app.state.monitortask.ram_stats

    return GetRamResponseSchema(
        total = ram_stats.get('total', 0),
        used=ram_stats.get('used', 0),
        free=ram_stats.get('free', 0),
        percent=ram_stats.get('percent', 0.0)
    )
