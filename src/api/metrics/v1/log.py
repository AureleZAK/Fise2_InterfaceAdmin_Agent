"""
This module defines API routes for handling CPU-related data.
"""
from fastapi import APIRouter, Request
from domain.schemas import (
    ExceptionResponseSchema,
    GetLogResponseSchema,
)
from domain.services import LogService

log_router = APIRouter()


@log_router.get(
    "",
    response_model=GetLogResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_log(request: Request) -> GetLogResponseSchema:
    """
    Route to get a list of CPU data.

    Args:
        request (Request): The incoming request.

    Returns:
        List[GetCpuResponseSchema]: A list of CPU data as per the response model.
    """
    return await LogService().get_log()


