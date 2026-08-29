from uuid import uuid4

from fastapi import HTTPException

from app.core.enums import PostSourceType
from app.database import SessionLocal
from app.models.post import Post


class IngestService:
    def create_post(self, *, source_type: str, source_url: str | None, markdown: str | None):
        raw_content = markdown or source_url or ""
        if not raw_content:
            raise HTTPException(status_code=400, detail="Provide either source_url or markdown")

        post = Post(
            id=str(uuid4()),
            source_type=PostSourceType(source_type),
            source_url=source_url,
            markdown=markdown,
            raw_content=raw_content,
        )

        db = SessionLocal()
        db.add(post)
        db.commit()
        db.refresh(post)
        db.close()
        return post
