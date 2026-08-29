from fastapi import APIRouter, HTTPException

from app.services.review_service import ReviewService

router = APIRouter(prefix="/api/v1/review", tags=["review"])


@router.post("/approve/{variant_id}")
def approve_variant(variant_id: str):
    variant = ReviewService().approve(variant_id)
    return {"variant_id": variant.id, "status": variant.status.value}


@router.post("/reject/{variant_id}")
def reject_variant(variant_id: str, reason: str = "Rejected by reviewer"):
    variant = ReviewService().reject(variant_id, reason)
    return {"variant_id": variant.id, "status": variant.status.value, "reason": reason}
