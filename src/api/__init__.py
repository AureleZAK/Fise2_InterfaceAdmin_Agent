from fastapi import APIRouter
from api.metrics.v2.ram import ram_router as ram_v2_router
from api.metrics.v1.cpu import cpu_router as cpu_v1_router

router = APIRouter()
router.include_router(ram_v2_router, prefix="/metrics/v2/ram")
router.include_router(cpu_v1_router, prefix="/metrics/v1/cpu")
__all__ = ["router"]

