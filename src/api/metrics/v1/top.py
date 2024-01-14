# src/api/metrics/v1/top.py

from fastapi import APIRouter, Request

from domain.schemas import (
    ExceptionResponseSchema,
    TopProcessesResponseSchema,
)
from domain.services import TopProcessesService

top_router = APIRouter()
top_processes_service = TopProcessesService()

@top_router.get(
    "/processes",
    response_model=TopProcessesResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_top_processes(request: Request) -> TopProcessesResponseSchema:
    """
    Route to get the top CPU and memory-consuming processes.
    """
    return await top_processes_service.get_top_processes(request.app.state.monitortask)
