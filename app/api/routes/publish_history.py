from fastapi import APIRouter

from app.database import SessionLocal
from app.models.publish_history import PublishHistory

router = APIRouter(prefix="/api/v1/history", tags=["history"])


@router.get("/{variant_id}")
def get_history_for_variant(variant_id: str):
    db = SessionLocal()
    rows = db.query(PublishHistory).filter(PublishHistory.variant_id == variant_id).all()
    records = [
        {
            "id": row.id,
            "platform": row.platform,
            "result": row.result,
            "external_post_url": row.external_post_url,
        }
        for row in rows
    ]
    db.close()
    return records
