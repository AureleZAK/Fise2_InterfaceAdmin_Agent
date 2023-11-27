"""
This module defines API routes for handling CPU-related data.
"""
from typing import List
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetCpuResponseSchema,
    GetCpuCoreResponseSchema,
)
from domain.services import CpuService

ram_router = APIRouter()


@ram_router.get(
    "/usage",
    response_model=List[GetCpuResponseSchema],
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def ram_usage(request: Request) -> List[GetCpuResponseSchema]:
    """
    Get the percent of used ram

    Args:
        request (Request): The incoming request.

    Returns:
        Percent used
    """
    return await RamService().get_cpu(request.app.state.monitortask)
