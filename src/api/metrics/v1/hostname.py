"""
This module defines API routes for handling RAM-related data.
"""
from fastapi import APIRouter, Request

from domain.schemas import (
    ExceptionResponseSchema,
    GetHostnameResponseSchema,
)
from domain.services import HostService

host_router = APIRouter()
hostservice = HostService()

@host_router.get(
    "",
    response_model= GetHostnameResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
)

async def get_hostname( request : Request) -> GetHostnameResponseSchema:
    """

    Route to get the hostname of the server.

    """
    #hostname = await hostservice.get_hostname(request)
    return GetHostnameResponseSchema(hostname = request.app.state.monitortask.hostname_info)
