"""
This module defines API routes for handling Disk-related data.
"""
from fastapi import APIRouter, Request

from domain.schemas import (
    ExceptionResponseSchema,
    GetDiskResponseSchema,
)
from domain.services import DiskService

disk_router = APIRouter()
diskservice = DiskService()

@disk_router.get(
    "/",
    response_model= GetDiskResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)

async def get_disk( request : Request) -> GetDiskResponseSchema:
    """

    Route to get the Disk usage stats

    """
    return await DiskService().get_disk(request.app.state.monitortask)