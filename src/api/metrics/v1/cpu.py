"""
This module defines API routes for handling CPU-related data.
"""
from typing import List
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetCpuResponseSchema,
    GetCpuCoreResponseSchema,
    GetCpuAvgLoadResponseSchema,
)
from domain.services import CpuService

cpu_router = APIRouter()


@cpu_router.get(
    "/usage",
    response_model=List[GetCpuResponseSchema],
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_cpu(request: Request) -> List[GetCpuResponseSchema]:
    """
    Route to get a list of CPU data.

    Args:
        request (Request): The incoming request.

    Returns:
        List[GetCpuResponseSchema]: A list of CPU data as per the response model.
    """
    return await CpuService().get_cpu(request.app.state.monitortask)


@cpu_router.get(
    "/core",
    response_model=GetCpuCoreResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_core_number(request: Request) -> GetCpuCoreResponseSchema:
    """
    Route to get the number of CPU core.

    Args:
        request (Request): The incoming request.

    Returns:
        int: number of cpu core.
    """
    return GetCpuCoreResponseSchema(number=request.app.state.monitortask.num_cores)

@cpu_router.get(
    "/avg-load",
    response_model=GetCpuAvgLoadResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_avg_load(request: Request) -> GetCpuAvgLoadResponseSchema:
    """
    Route to get the percentage representation of the average system load

    Args:
        request (Request): The incoming request.

    Returns:
        list[float]: average system load (%)
    """
    return GetCpuAvgLoadResponseSchema(avgLoad=request.app.state.monitortask.cpu_avg_load_percentage)