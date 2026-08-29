from fastapi import APIRouter

from app.services.constraint_validator import ConstraintValidator
from app.services.variant_generator import VariantGenerator

router = APIRouter(prefix="/api/v1/variants", tags=["variants"])


@router.post("/generate")
def generate_variant(post_id: str, platform: str, tone: str = "professional"):
    variant = VariantGenerator().generate_for_post(post_id, platform, tone)
    ConstraintValidator().validate(variant)
    return {"id": variant.id, "status": variant.status.value, "content": variant.content}
