from fastapi import HTTPException

from app.core.enums import VariantStatus
from app.database import SessionLocal
from app.models.variant import Variant


class ReviewService:
    def approve(self, variant_id: str):
        db = SessionLocal()
        variant = db.query(Variant).filter(Variant.id == variant_id).first()
        if not variant:
            raise HTTPException(status_code=404, detail="Variant not found")

        variant.status = VariantStatus.APPROVED
        db.commit()
        db.refresh(variant)
        db.close()
        return variant

    def reject(self, variant_id: str, reason: str):
        db = SessionLocal()
        variant = db.query(Variant).filter(Variant.id == variant_id).first()
        if not variant:
            raise HTTPException(status_code=404, detail="Variant not found")

        variant.status = VariantStatus.REJECTED
        variant.validation_errors = reason
        db.commit()
        db.refresh(variant)
        db.close()
        return variant
