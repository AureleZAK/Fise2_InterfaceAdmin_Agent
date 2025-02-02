"""
Ce module définit les routes pour les métriques de l'API.

Routes disponibles :
- `/metrics/v1/cpu` : Routes pour les métriques CPU.
- `/metrics/v1/ram` : Routes pour les métriques RAM.
- `/metrics/v1/ip` : Routes pour les métriques IP.
- `/metrics/v1/hostname` : Routes pour les métriques de nom d'hôte.
- `/metrics/v1/disk` : Routes pour les métriques Disk
"""
from fastapi import APIRouter
from api.metrics.v1.cpu import cpu_router as cpu_v1_router
from api.metrics.v1.ram import ram_router as ram_v1_router
from api.metrics.v1.ip import ip_router as ip_v1_router
from api.metrics.v1.hostname import host_router as host_v1_router
from api.metrics.v1.log import log_router as log_v1_router
from api.metrics.v1.disk import disk_router as disk_v1_router

router = APIRouter()
router.include_router(cpu_v1_router, prefix="/metrics/v1/cpu")
router.include_router(ram_v1_router, prefix="/metrics/v1/ram")
router.include_router(ip_v1_router, prefix="/metrics/v1/ip")
router.include_router(host_v1_router, prefix="/metrics/v1/hostname")
router.include_router(log_v1_router, prefix="/metrics/v1/log")
router.include_router(disk_v1_router, prefix="/metrics/v1/disk")

__all__ = ["router"]
