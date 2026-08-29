from fastapi import APIRouter

from app.schemas.post import PostCreate
from app.services.ingest_service import IngestService

router = APIRouter(prefix="/api/v1/posts", tags=["posts"])


@router.post("/ingest")
def ingest_post(payload: PostCreate):
    service = IngestService()
    post = service.create_post(
        source_type=payload.source_type,
        source_url=payload.source_url,
        markdown=payload.markdown,
    )
    return {"id": post.id, "message": "stored"}
