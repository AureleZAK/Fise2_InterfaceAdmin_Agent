"""
This module defines API routes for handling RAM-related data.
"""
from fastapi import APIRouter, Request

from domain.schemas import (
    ExceptionResponseSchema,
    GetHostnameResponseSchema,
)
from domain.services import HostService
import socket

host_router = APIRouter()
host_service = HostService()

@host_router.get(
    "/hostname",
    response_model= GetHostnameResponseSchema,
    # response_model_exclude={"id"},
    responses={"400": {"model": ExceptionResponseSchema}},
) 

async def get_hostname( request : Request):
    """

    Route to get the hostname of the server.

    """
    hostname = socket.gethostname()
    return {"hostname" : hostname}