from datetime import datetime, timezone

from fastapi import APIRouter

status_router = APIRouter(tags=["Status"])


@status_router.get("/ping")
def status_ping():
    """Ping the API"""
    return {"ping": "pong"}


@status_router.get("/health")
def status_health():
    """Check the health of the Api"""
    utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    return {
        "status": "success",
        "utc": utc,
    }
