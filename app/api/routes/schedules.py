from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.core.enums import VariantStatus
from app.database import SessionLocal
from app.models.variant import Variant

router = APIRouter(prefix="/api/v1/schedules", tags=["schedules"])


@router.post("/")
def create_schedule(variant_id: str, scheduled_for: datetime):
    db = SessionLocal()
    variant = db.query(Variant).filter(Variant.id == variant_id).first()
    if not variant:
        raise HTTPException(status_code=404, detail="Variant not found")

    if variant.status != VariantStatus.APPROVED:
        raise HTTPException(
            status_code=400,
            detail="Variant must be approved before scheduling",
        )

    return {"message": "scheduled", "variant_id": variant.id, "scheduled_for": scheduled_for.isoformat()}
