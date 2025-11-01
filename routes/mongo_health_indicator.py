# app/routers/mongo_router.py
from fastapi import APIRouter, HTTPException
from formative_1_ml_pipeline.crud.mongo_crud_health_indicator import (
    create_health_indicator as create_indicator_crud,
    get_health_indicator as get_indicator_crud,
    update_health_indicator as update_indicator_crud,
)
from formative_1_ml_pipeline.model.mongo_schema import HealthIndicator

router = APIRouter(prefix="/mongo", tags=["MongoDB CRUD"])

@router.post("/health-indicators")
async def create_health_indicator(indicator: HealthIndicator):
    new_id = await create_indicator_crud(indicator.dict(exclude_unset=True))
    return {"_id": new_id}

@router.put("/health-indicators/{indicator_id}")
async def update_health_indicator(indicator_id: str, indicator: HealthIndicator):
    updated = await update_indicator_crud(indicator_id, indicator.dict(exclude_unset=True))
    return updated
