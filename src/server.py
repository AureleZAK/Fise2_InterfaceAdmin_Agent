"""
This module contains a FastAPI application with various routes and middleware.

It initializes the FastAPI app, sets up routers, event listeners, and exception handlers, and
creates a monitoring thread for fetching metrics.
"""
import threading
from typing import List
from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from api import router
from api.default.default import default_router
from core.exceptions import CustomException
from core.config import get_config
from monitor import MonitorTask
import apache_log_parser
from datetime import datetime


def init_routers(fastapi: FastAPI) -> None:
    """
    Initialize API routers and include them in the FastAPI fastapi.

    Args:
        fastapi (FastAPI): The FastAPI application to add routers to.
    """
    # Add default route (version, healthcheck)
    fastapi.include_router(default_router)
    # Add domain routes
    fastapi.include_router(router)


def init_listeners(fastapi: FastAPI) -> None:
    """
    Initialize event listeners and exception handlers for the FastAPI fastapi.

    Args:
        fastapi (FastAPI): The FastAPI application to set up event listeners and handlers for.
    """
    # Exception handler
    @fastapi.exception_handler(CustomException)
    async def custom_exception_handler(_request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )

    # Start monitoring thread
    @fastapi.on_event("startup")
    def on_start_up():
        thread = threading.Thread(target=fastapi.state.monitortask.monitor, daemon=True)
        thread.start()


def make_middleware() -> List[Middleware]:
    """
    Create and return a list of middleware components, including CORS middleware.

    Returns:
        List[Middleware]: List of FastAPI middleware components.
    """
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    ]
    return middleware

def count_log(log_file):


    unique_ips = set()
    cpt404 = 0
    cpt200 = 0
    page_visits = {}

    try:

        with open(log_file, 'r') as file:
            for line in file:
                log_entry = log_parser(line)
                ip = log_entry[0]
                status = log_entry[3]
                request_url = log_entry[2]
                request_url_split = request_url.split()[1]
                page_visits[request_url_split] = page_visits.get(request_url_split,0)+1
                if (status == '404'):
                    cpt404 = cpt404 + 1
                else:
                    cpt200 = cpt200 + 1

                if (ip != '127.0.0.1'):
                    unique_ips.add(ip)



        return len(unique_ips), cpt200, cpt404, page_visits
    except FileNotFoundError:
        print(f"Le fichier {log_file} n'a pas été trouvé.")
        return None

def log_parser(log_entry):
    log_format = '%v %h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"'
    parser = apache_log_parser.make_parser(log_format)

    parsed_data = parser(log_entry)
    result_log = [
        parsed_data.get('remote_host', ''),
        parsed_data.get('time_received', ''),
        parsed_data.get('request_first_line', ''),
        parsed_data.get('status', '')
    ]

    return result_log



def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: The configured FastAPI application.
    """
    config = get_config()
    # Monitoring thread to fetch metrics
    monitortask = MonitorTask()
    # API
    fastapi = FastAPI(
        title=config.title,
        description=config.description,
        version=config.version,
        docs_url="/docs",
        redoc_url="/redoc",
        middleware=make_middleware(),
    )
    fastapi.state.monitortask = monitortask
    fastapi.state.version = config.version
    init_routers(fastapi)
    init_listeners(fastapi)
    return fastapi


app = create_app()
