from fastapi import APIRouter

from app.api.schemas import HealthResponse

router = APIRouter(tags=["actuator"])


@router.get("/actuator/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="UP")
